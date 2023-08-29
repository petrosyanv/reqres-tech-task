import json
from typing import Any, Optional


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