import json as json_lib
from json import JSONDecodeError
from typing import Any, BinaryIO, Callable, Dict, Optional

import requests
from marshmallow import ValidationError

from api.entities.json_helper import JsonHelper


class ApiClient:
    def __init__(
        self, url: str, headers: Dict = None, timeout: float = None, ssl: bool = True
    ):
        self.url = url
        self.headers = headers
        self.timeout = timeout
        self.ssl = ssl

    def _get(
        self,
        endpoint: str = "",
        dto: Any = None,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        headers: Optional[Dict] = None,
        is_form_data: bool = False,
        query_params: Optional[Any] = None,
        ignore_parse_exception: bool = False,
    ) -> Any:
        return self._send_request(
            method=requests.get,
            endpoint=endpoint,
            dto=dto,
            expected_type=expected_type,
            error_type=error_type,
            headers=headers,
            files=None,
            is_form_data=is_form_data,
            query_params=query_params,
            ignore_parse_exception=ignore_parse_exception,
        )

    def _post(
        self,
        endpoint: str = "",
        dto: Any = None,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        headers: Optional[Dict] = None,
        files: Optional[list[tuple[str, tuple[str, BinaryIO, str]]]] = None,
        is_form_data: bool = False,
        query_params: Optional[Any] = None,
        ignore_parse_exception: bool = False,
    ) -> Any:
        return self._send_request(
            method=requests.post,
            endpoint=endpoint,
            dto=dto,
            expected_type=expected_type,
            error_type=error_type,
            headers=headers,
            files=files,
            is_form_data=is_form_data,
            query_params=query_params,
            ignore_parse_exception=ignore_parse_exception,
        )

    def _put(
        self,
        endpoint: str = "",
        dto: Any = None,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        headers: Optional[Dict] = None,
        files: Optional[list[tuple[str, tuple[str, BinaryIO, str]]]] = None,
        is_form_data: bool = False,
        query_params: Optional[Any] = None,
        ignore_parse_exception: bool = False,
    ) -> Any:
        return self._send_request(
            method=requests.put,
            endpoint=endpoint,
            dto=dto,
            expected_type=expected_type,
            error_type=error_type,
            headers=headers,
            files=files,
            is_form_data=is_form_data,
            query_params=query_params,
            ignore_parse_exception=ignore_parse_exception,
        )

    def _patch(
        self,
        endpoint: str = "",
        dto: Any = None,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        headers: Optional[Dict] = None,
        files: Optional[list[tuple[str, tuple[str, BinaryIO, str]]]] = None,
        is_form_data: bool = False,
        query_params: Optional[Any] = None,
        ignore_parse_exception: bool = False,
    ) -> Any:
        return self._send_request(
            method=requests.patch,
            endpoint=endpoint,
            dto=dto,
            expected_type=expected_type,
            error_type=error_type,
            headers=headers,
            files=files,
            is_form_data=is_form_data,
            query_params=query_params,
            ignore_parse_exception=ignore_parse_exception,
        )

    def _delete(
        self,
        endpoint: str = "",
        dto: Any = None,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        headers: Optional[Dict] = None,
        files: Optional[list[tuple[str, tuple[str, BinaryIO, str]]]] = None,
        is_form_data: bool = False,
        query_params: Optional[Any] = None,
        ignore_parse_exception: bool = False,
    ) -> Any:
        return self._send_request(
            method=requests.delete,
            endpoint=endpoint,
            dto=dto,
            expected_type=expected_type,
            error_type=error_type,
            headers=headers,
            files=files,
            is_form_data=is_form_data,
            query_params=query_params,
            ignore_parse_exception=ignore_parse_exception,
        )

    def _send_request(
        self,
        method: Callable,
        endpoint: str = "",
        dto: Any = None,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        headers: Optional[Dict] = None,
        files: Optional[list[tuple[str, tuple[str, BinaryIO, str]]]] = None,
        is_form_data: bool = False,
        query_params: Any = None,
        ignore_parse_exception: bool = False,
    ) -> Any:
        request_headers = self._prepare_headers(headers)
        payload = None if dto is None else self._prepare_payload(dto)
        query = self._prepare_query_params(query_params)
        url = f"{self.url}/{endpoint}{query}"

        if is_form_data:
            res = method(
                url,
                data=payload,
                headers=request_headers,
                timeout=self.timeout,
                verify=self.ssl,
                files=files,
            )
        else:
            res = method(
                url,
                json=payload,
                headers=request_headers,
                timeout=self.timeout,
                verify=self.ssl,
                files=files,
            )

        return self._expected_or_error(
            res.text, expected_type, error_type, ignore_parse_exception
        )

    # returns the expected type, returns the error alternatively (if set)
    @staticmethod
    def _expected_or_error(
        res: Any,
        expected_type: Optional[Any] = None,
        error_type: Optional[Any] = None,
        ignore_parse_exception: bool = False,
    ):
        try:
            if expected_type is None:
                return None
            return JsonHelper.from_json(res, expected_type, ignore_parse_exception)
        except ValidationError as ex_expected_type:
            try:
                if error_type is None:
                    raise ex_expected_type
                return JsonHelper.from_json(res, error_type, ignore_parse_exception)
            except ValidationError as ex_error_type:
                raise Exception(
                    f"Could not convert to any of the types provided:\n"
                    f"Expected Type:\n"
                    f"{ex_expected_type}\n"
                    f"Error Type:\n"
                    f"{ex_error_type}\n"
                )

    def _prepare_headers(self, headers: Optional[Dict]) -> Dict:
        request_headers = {} if self.headers is None else self.headers.copy()
        if headers is not None:
            request_headers.update(headers)
        return request_headers

    @staticmethod
    def _prepare_payload(dto):
        payload = JsonHelper.to_json(dto)
        try:
            payload = json_lib.loads(payload)
        except TypeError:
            pass
        except JSONDecodeError:
            return payload
        return payload

    @staticmethod
    def _prepare_query_params(query_data: Any) -> str:
        if query_data is None:
            return ""

        query_dict = JsonHelper.to_json_dict(query_data)
        url = "?"
        if query_dict is not None:
            for k, v in query_dict.items():
                if v == "":
                    url += f"{k}"
                elif v is not None:
                    url += f"{k}={v}&"

        if url[-1] == "?" or url[-1] == "&":
            url = url[:-1]

        return url
