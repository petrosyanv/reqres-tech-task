from config import Configurator
from new_api.controllers.api_client_new import ApiClient
from new_api.tests.steps.get_products_steps import step_get_products, step_get_product


class Test:

    def test_get(self, config: Configurator, api_client: ApiClient):
        products = step_get_product(
            product_id=1,
            basic_url=config.TEST_URL,
            api_client=api_client
        )
        print(products.title)
        return products
