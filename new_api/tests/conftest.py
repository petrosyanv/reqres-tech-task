import pytest


from config import Configurator
from new_api.controllers.api_client_new import ApiClient

@pytest.fixture(scope="session", autouse=True)
def config() -> Configurator:
    return Configurator()

@pytest.fixture(scope="session", autouse=True)
def api_client() -> ApiClient:
    return ApiClient()


