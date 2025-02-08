import json

from api.entities.api_client_new import ApiClientNew
from typing import Dict, Any
import requests

from models.model_booker import Booking, UpdateBooking, PatchBooking


class ApiClientBooker(ApiClientNew):

    def __init__(self, url: str, timeout: float = None, ssl: bool = False):
        super(ApiClientBooker, self).__init__(url=f"{url}", timeout=timeout, ssl=ssl)

    def get_booking(self):
        return super()._get(
            endpoint='booking',
            headers={'Content-Type': 'application/json'}
        )
    def get_booking_ids(self, id: int) -> Booking:
        return super()._get(
            endpoint=f"booking/{id}",
            headers={'Content-Type': 'application/json'},
            expected_type=Booking,
            error_type=Booking
        )

    def post_booking(self, dto: Booking):
        return super()._post(
            endpoint='booking',
            dto=dto,
            expected_type=UpdateBooking,
            error_type=UpdateBooking,
            headers={'Content-Type': 'application/json'},
        )

    def put_booking(self, dto: Booking, id: int):
        return super()._put(
            endpoint=f"booking/{id}",
            dto=dto,
            headers={'Content-Type': 'application/json'},
            expected_type=Booking,
            error_type=Booking
        )

    def patch_booking(self, dto: Booking, id: int):
        return super()._patch(
            endpoint=f"booking/{id}",
            dto=dto,
            headers={'Content-Type': 'application/json'},
            expected_type=PatchBooking,
            error_type=PatchBooking
        )

    def delete_booking(self, id: int):
        return super()._delete(
            endpoint=f"booking/{id}",
            headers={'Content-Type': 'application/json'},
        )



