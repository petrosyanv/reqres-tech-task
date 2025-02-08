from dataclasses import dataclass, field
from typing import Optional, Any, Dict
from dataclasses_json import config, dataclass_json, LetterCase


@dataclass
@dataclass_json()
class Activities:
    id: int = field(metadata=config(field_name="id"))
    title: str = field(metadata=config(field_name="title"))
    dueDate: str = field(metadata=config(field_name="dueDate"))
    completed: bool = field(metadata=config(field_name="completed"))


@dataclass
@dataclass_json()
class Authors:
    id: Optional[int] = field(default=None)
    idBook: Optional[int] = field(default=None, metadata=config(field_name="idBook"))
    firstName: Optional[str] = field(default=None, metadata=config(field_name="firstName"))
    lastName: Optional[str] = field(default=None, metadata=config(field_name="lastName"))

@dataclass_json
@dataclass
class Books:
    id: int = field(default=None)
    title: str = field(default=None)
    description: str = field(default=None)
    pageCount: int = field(default=None)
    excerpt: str = field(default=None)
    publishDate: str = field(default=None)


@dataclass_json
@dataclass
class CoverBooks:
    id: int = field(default=None)
    id_books: int = field(default=None)
    url: str = field(default=None)


@dataclass_json
@dataclass
class Users:
    id: int = field(default=None)
    userName: str = field(default=None)
    password: str = field(default=None)


