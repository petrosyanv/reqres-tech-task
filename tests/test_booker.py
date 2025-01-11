from api.entities.api_client_booker import ApiClientBooker
from config import Configurator
from models import model_booker


class TestBooker:
    config = Configurator()
    api_client = ApiClientBooker(url=config.BOOKER_URL)

    def test_all_ids(self):
        response = self.api_client.get_booking()
        print(response)
