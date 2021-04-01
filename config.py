import os
from configparser import ConfigParser


class Configurator:

    def __init__(self):
        config = ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

        #API
        self.BASE_URL = config.get('api', 'base_url')