import json.decoder
from json.decoder import JSONDecodeError

import requests

from common.logger_basic_config import get_configured_logger
from config import Configurator

LOG = get_configured_logger('caller')


class Caller:

    config = Configurator()

    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    @staticmethod
    def __clean_nones_from_dict(dictionary: dict):
        new_dict = {}
        for k, v in dictionary.items():
            if v is None:
                pass
            else:
                new_dict[k] = v
        return new_dict

    def call(self, method, uri, params=None, body=None):
        body = {} if body is None else body
        body = self.__clean_nones_from_dict(body)
        response = self.session.request(
            url=self.base_url + uri,
            method=method,
            params=params,
            data=json.dumps(body),
            headers=self.headers
        )

        try:
            resp_to_log = json.dumps(json.loads(response.text), indent=4)
        except JSONDecodeError:
            resp_to_log = response.text
        try:
            body_to_log = json.dumps(body, indent=4)
        except JSONDecodeError:
            body_to_log = body
        response_log = f'CALLER {method.upper()}:{response.request.url}\nPARAMS: {params}\nBODY: {body_to_log}' \
                       f'\n\nRESPONSE CODE: {response.status_code} \nRESPONSE BODY: {resp_to_log}'
        LOG.info(response_log)

        return response


class ResponseError(Exception):

    pass


