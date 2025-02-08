import re
from api.entities.api_client_faker import ApiClientFaker
import pytest

from config import Configurator


class TestFaker:



    @classmethod
    def setup_class(cls):
        cls.conf = Configurator()
        cls.api_client = ApiClientFaker(url=cls.conf.FAKER_URL)

    def test_get_activities(self):
        response = self.api_client.get_authors_id(1)
        print(response)
