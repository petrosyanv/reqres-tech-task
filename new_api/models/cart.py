from dataclasses import dataclass, field
from typing import Optional, Any, Dict
from dataclasses_json import config, dataclass_json, LetterCase

from new_api.models.product import Product


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Cart:
    id: int
    products: Dict[Product]
    total: int
    discountTotal: int
    user_id: int
    total_products: int
    total_quantity: int

