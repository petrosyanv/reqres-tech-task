import pytest

from config import Configurator
from new_api.controllers.api_client_new import ApiClient
from new_api.tests.steps.add_products_steps import step_prepare_product, step_add_product
from new_api.tests.steps.get_products_steps import step_get_products, step_get_product


class Test:
    @pytest.mark.parametrize(
       "id, title, price",
       [
           (6, 'MacBook Pro', 1749),
           (7, 'Samsung Galaxy Book', 1499),
           (8, 'Microsoft Surface Laptop 4', 1499),
           (9, 'Infinix INBOOK', 1099)

       ])
    def test_get(self, id, title, price,  config: Configurator, api_client: ApiClient):
        products = step_get_product(
            product_id=id,
            basic_url=config.TEST_URL,
            api_client=api_client
        )
        assert products.title == title
        assert products.price == price

    def test_post(self, config: Configurator, api_client: ApiClient):
        product = step_prepare_product()
        response_product = step_add_product(
            basic_url=config.TEST_URL,
            api_client=api_client,
            product=product
        )
        assert product.title == response_product.title

