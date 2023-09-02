from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import config, dataclass_json, LetterCase


from new_api.models.product import Product


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Products:
    products: List[Product]
    total: int
    skip: int
    limit: int
