from new_api.controllers.api_client_new import ApiClient
from new_api.models.product import Product
from new_api.models.products import Products


def step_get_product(
        basic_url,
        api_client: ApiClient,
        product_id
) -> Product:
    return api_client.get_product(id=product_id, basic_url=basic_url)


def step_get_products(
        basic_url,
        api_client: ApiClient,
) -> Products:
    return api_client.get_products(basic_url=basic_url)


def step_get_category(
        basic_url,
        api_client: ApiClient,
        category
) -> Products:
    return api_client.get_category(category=category, basic_url=basic_url)


def step_get_categories(
        basic_url,
        api_client: ApiClient,
):
    return api_client.get_categories(basic_url=basic_url)
