from api.controllers.users import Users
from api.controllers.caller import Caller
from config import Configurator


class ApiClient:

    def __init__(self):
        self._caller = Caller(Configurator().BASE_URL)
        self.users = Users(self._caller)
