from dataclasses import dataclass, field
from typing import Optional, Any, Dict
from dataclasses_json import config, dataclass_json


@dataclass
class Bookingdates:
    checkin: str
    checkout: str

@dataclass_json
@dataclass
class Booking:
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: Bookingdates
    additionalneeds: Optional[str]= field(default=None)
