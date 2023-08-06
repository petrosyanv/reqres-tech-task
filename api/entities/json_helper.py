import json
import json as json_lib
from json import JSONDecodeError
from typing import Any, Dict, Optional, get_args, get_origin

from marshmallow.exceptions import ValidationError


class JsonHelper:
    @staticmethod
    def to_json(data: Any) -> Optional[str]:
        # is None
        if data is None:
            return None

        # is list
        if isinstance(data, list):
            if len(data) > 0:
                formatted = ",".join([f'"{JsonHelper.to_json(d)}"' for d in data])
                return f"[{formatted}]"
            else:
                return "[]"

        # is dictionary
        if hasattr(data, "__dict__"):
            return data.to_json()
        if isinstance(data, dict):
            return json.dumps(data)

        # is primitive
        return str(data)

    @staticmethod
    def from_json(
        json: str, target_type: Optional[Any] = None, except_disable: bool = False
    ) -> Any:
        # target type is not supplied
        if target_type is None:
            try:
                # is dictionary
                return json_lib.loads(json)
            except JSONDecodeError:
                # is primitive
                return json

        try:
            # is list
            if get_origin(target_type) is list:
                contained_type = get_args(target_type)[0]
                if hasattr(contained_type, "schema") and callable(
                    getattr(contained_type, "schema")
                ):
                    # If the contained type has a 'schema' method, use it
                    return contained_type.schema().loads(json, many=True)
                else:
                    # Handle the case when the contained type doesn't have a 'schema' method
                    # Perform the necessary operations based on the type
                    # For example, you can manually deserialize the JSON using the contained_type
                    return [contained_type(item) for item in json]
            # is instance
            return target_type.schema().loads(json)
        except (ValidationError, KeyError) as err:
            try:
                # is dictionary
                if target_type is dict or except_disable:
                    return json_lib.loads(json)
                else:
                    raise err
            except JSONDecodeError:
                # is primitive
                return json

    @staticmethod
    def to_json_dict(data: Any) -> Optional[Dict]:
        json_str = JsonHelper.to_json(data)
        json_dict = json.loads(json_str)
        return json_dict
