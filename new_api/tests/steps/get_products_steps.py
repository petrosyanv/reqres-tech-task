from new_api.controllers.api_client_new import ApiClient
from new_api.models.product import Product
from new_api.models.products import Products


def step_get_product(
        api_client: ApiClient,
        product_id
) -> Product:
    return api_client.get_product(id=product_id)


def step_get_products(
        api_client: ApiClient,
) -> Products:
    return api_client.get_products()


def step_get_category(
        api_client: ApiClient,
        category
) -> Products:
    return api_client.get_category(category=category)


def step_get_categories(
        api_client: ApiClient,
):
    return api_client.get_categories()
