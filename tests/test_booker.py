from api.entities.api_client_booker import ApiClientBooker
from config import Configurator
from models.model_booker import Booking, Bookingdates, UpdateBooking


class TestBooker:
    config = Configurator()
    api_client = ApiClientBooker(url=config.BOOKER_URL)

    def test_all_ids(self):
        response = self.api_client.get_booking_ids(2)
        assert response.lastname == "Ericsson"
        assert response.firstname == "Susan"

    def test_post_valid_date(self):
        post_info = Booking(
            firstname="Barbara",
            lastname="Mroz",
            totalprice=300,
            depositpaid=100,
            bookingdates=Bookingdates(
                checkin="2023-02-23",
                checkout="2023-10-23"
            ),
            additionalneeds="lunch"
        )
        response = self.api_client.post_booking(post_info)
        print(response)
        assert response.booking.lastname == "Mroz"

    def test_post_invalid_date(self):
        post_info = Booking(
            firstname="Barbara",
            lastname="Mroz",
            totalprice=300,
            depositpaid=100,
            bookingdates=Bookingdates(
                checkin="2024-yu3",
                checkout="2023hj0/23"
            ),
            additionalneeds="lunch"
        )
        response = self.api_client.post_booking(post_info)
        print(response)
        assert response.booking.bookingdates.checkin == '0NaN-aN-aN'
        assert response.booking.bookingdates.checkout == '0NaN-aN-aN'

    # Verify
    # multiple
    # filters
    # applied
    # return correct
    # booking
    # IDs.
    def test_multiple_filters(self):
        response = self.api_client.get_booking_ids(3)
        response_2 = self.api_client.get_booking_ids(2)
        print(response, response_2)

    # Verify
    # booking
    # details
    # are
    # returned
    # with valid ID.
    # def test_valid_id(self):
    #     response = self.api_client.get_booking()

    # def test_put_booking(self):
    #     updated_booking = Booking(
    #         firstname="Susan",
    #         lastname="Ericsson",
    #         totalprice=597,
    #         depositpaid=True,
    #         bookingdates=Bookingdates(
    #             checkin="2021-06-12",
    #             checkout="2022-07-17"
    #         ),
    #         additionalneeds="Breakfast"
    #     )
    #
    #     put_info = UpdateBooking(
    #         booking_id=3,
    #         booking=updated_booking
    #     )
    #
    #     response = self.api_client.put_booking(put_info, 3)
    #     print(response)

    def test_put_booking(self):
        updated_booking = Booking(
            firstname="Barbara",
            lastname="Mroz",
            totalprice=300,
            depositpaid=100,
            bookingdates=Bookingdates(
                checkin="2024-12-09",
                checkout="2024-01-08"
            ),
            additionalneeds="lunch"
        )

        put_info = UpdateBooking(
            booking_id=3,
            booking=updated_booking
        )

        # Make the PUT request
        response = self.api_client.put_booking()
        print(response)

    def test_delete_booking(self):
        response = self.api_client.delete_booking(1)
        print(response)

        response_2 = self.api_client.get_booking_ids(1)
        print(response_2)
