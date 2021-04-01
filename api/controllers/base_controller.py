from config import Configurator
from api.controllers.caller import Caller


class BaseController:

    def __init__(self, caller: Caller):
        self._config = Configurator()
        self.caller = caller
