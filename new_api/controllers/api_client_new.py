import json as json_lib
from json import JSONDecodeError
from typing import Any, BinaryIO, Callable, Dict, Optional

import requests

from new_api.models.helper import JsonHelper
from new_api.models.product import Product
from new_api.models.products import Products

basic_url = "https://dummyjson.com/"
class ApiClient:
    def get_products(self):
        return requests.get(url=f"{basic_url}/products", verify=False)

    def get_product(self, id: int):
        return requests.get(url=f"{basic_url}/products/{id}", verify=False)

    def get_categories(self):
        return requests.get(url=f"{basic_url}/products/categories", verify=False)

    def get_category(self, category: str):
        return requests.get(url=f"{basic_url}/products/category/{category}", verify=False)

    def post_product(self, product: Product):
        return requests.post(
            data={"data": f"{JsonHelper.to_json(product)}"},
            verify=False,
            url=f"{basic_url}/products/add"
        )
    def put_product(self, product: Product, id: int):
        return requests.put(
            url=f"{basic_url}/products/{id}", verify=False,
            data={"data": f"{JsonHelper.to_json(product)}"}
        )

    def delete_product(self, id: int):
        return requests.delete(url=f"{basic_url}/products/{id}", verify=False)

