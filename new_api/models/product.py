from dataclasses import dataclass, field
from typing import Optional, Any
from dataclasses_json import config, dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Product:
    title: str
    description: str
    price: int
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    category: str
    id: Optional[int] = field(default=None)
    thumbnail: Optional[str] = field(default=None)
    images: Optional[Any] = field(default=None)

