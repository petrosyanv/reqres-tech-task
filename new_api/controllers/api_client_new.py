import json as json_lib
from json import JSONDecodeError
from typing import Any, BinaryIO, Callable, Dict, Optional

import requests

from new_api.models.helper import JsonHelper
from new_api.models.product import Product
from new_api.models.products import Products


class ApiClient:

    def get_products(self, basic_url) -> Products | Any:
        response = requests.get(url=f"{basic_url}/products", verify=False)
        return Products.from_dict(response.json())

    def get_product(self, basic_url, id: int) -> Product | Any:
        response = requests.get(url=f"{basic_url}/products/{id}", verify=False)
        return Product.from_dict(response.json())

    def get_categories(self, basic_url):
        return requests.get(url=f"{basic_url}/products/categories", verify=False)

    def get_category(self, basic_url, category: str):
        return requests.get(url=f"{basic_url}/products/category/{category}", verify=False)

    def post_product(self, basic_url, product: Product):
        return requests.post(
            data={"data": f"{JsonHelper.to_json(product)}"},
            verify=False,
            url=f"{basic_url}/products/add"
        )
    def put_product(self, basic_url, product: Product, id: int):
        return requests.put(
            url=f"{basic_url}/products/{id}", verify=False,
            data={"data": f"{JsonHelper.to_json(product)}"}
        )

    def delete_product(self, basic_url, id: int):
        return requests.delete(url=f"{basic_url}/products/{id}", verify=False)

