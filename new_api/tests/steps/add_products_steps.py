from config import Configurator
from new_api.controllers.api_client_new import ApiClient
from new_api.models.product import Product
from new_api.models.products import Products

def step_prepare_product(
        **kwargs
) -> Product:
    data = Product(
        title="iphone 13",
        description="An apple mobile which is nothing like apple",
        price=300,
        discount_percentage=30,
        rating=4.5,
        stock=50,
        brand="Apple",
        category="smartphones",
    )
    data.update(kwargs)
    return data


def step_add_product(
        api_client: ApiClient,
        product: Product
) -> Product:
    return api_client.post_product(product=product)


def step_update_product(
        api_client: ApiClient,
        product: Product,
        product_id
) -> Product:
    return api_client.put_product(product=product, id=product_id)