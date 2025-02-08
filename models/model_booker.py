from dataclasses import dataclass, field
from typing import Optional, Any, Dict
from dataclasses_json import config, dataclass_json, LetterCase

@dataclass
class Bookingdates:
    checkin: str = field(default=None, metadata=config(field_name="checkin"))
    checkout: str = field(default=None, metadata=config(field_name="checkout"))

@dataclass_json
@dataclass
class Booking:
    firstname: str = field(default=None, metadata=config(field_name="firstname"))
    lastname: str = field(default=None, metadata=config(field_name="lastname"))
    totalprice: int = field(default=None, metadata=config(field_name="totalprice"))
    depositpaid: bool = field(default=None, metadata=config(field_name="depositpaid"))
    bookingdates: Bookingdates = field(default=None, metadata=config(field_name="bookingdates"))
    additionalneeds: Optional[str] = field(default=None, metadata=config(field_name="additionalneeds"))

@dataclass_json
@dataclass
class UpdateBooking:
    booking_id: int = field(default=None, metadata=config(field_name="bookingid"))
    booking: Booking = field(default=None, metadata=config(field_name="booking"))

@dataclass_json
@dataclass
class PatchBooking:
    firstname: Optional[str] = field(default=None, metadata=config(field_name="firstname"))
    lastname: Optional[str] = field(default=None, metadata=config(field_name="lastname"))
    totalprice: Optional[int] = field(default=None, metadata=config(field_name="totalprice"))
    depositpaid: Optional[bool] = field(default=None, metadata=config(field_name="depositpaid"))
    bookingdates: Optional[Bookingdates] = field(default=None, metadata=config(field_name="bookingdates"))
    additionalneeds: Optional[str]= field(default=None, metadata=config(field_name="bookingdates"))

