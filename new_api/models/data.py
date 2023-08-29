from dataclasses import dataclass
from typing import Dict

@dataclass
class User:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

@dataclass
class Data:
    page: int
    per_page: int
    total: int
    total_pages: int

    data: Dict[User]

