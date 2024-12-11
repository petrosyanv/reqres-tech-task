from api.entities.api_client_new import ApiClientNew
from typing import Dict, Any

class ApiClientBooker(ApiClientNew):

    def __init__(self, url: str, headers: Dict = None, timeout: float = None, ssl: bool = True
    ):
        if headers is None:
            headers = {}
            headers.update(
                {
                    "Content- Type": "application/json"
                }
            )
        super().__init__(url=f"{url}", headers=headers, timeout=timeout, ssl=ssl)

    def get_auth_token(self, dto: Any) -> Any:
        return super()._post("auth", dto=dto)

