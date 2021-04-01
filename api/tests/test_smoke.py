import re
from api.entities.api_client import ApiClient
from api.entities.user import User
from common.utility import REGEX_EMAIL, REGEX_ONLY_LETTERS
import pytest


class TestSmoke:

    @classmethod
    def setup_class(cls):
        cls.api_client = ApiClient()

    def test_check_that_user_exist(self, status_code_ok):
        response = self.api_client.users.get_user(user_id=7, status_code=status_code_ok)
        assert response.user_id == 7
        assert re.search(REGEX_EMAIL, response.user_email)
        assert re.search(REGEX_ONLY_LETTERS, response.user_first_name)
        assert re.search(REGEX_ONLY_LETTERS, response.user_last_name)

    def test_check_that_user_does_not_exist(self, status_code_not_found):
        response = self.api_client.users.get_user(user_id=99, status_code=status_code_not_found)
        assert response.user_id is 0
        assert response.user_first_name is None
        assert response.user_last_name is None
        assert response.user_email is None
        assert response.user_avatar_link is None

    def test_user_creation(self, generate_user):
        user = self.api_client.users.create(generate_user)
        assert generate_user == user
        self.api_client.users.delete(user)

    def test_check_the_list_of_exist_users(self):
        response = self.api_client.users.get_all_users()
        for user in response:
            assert re.search(REGEX_EMAIL, user.user_email)
            assert re.search(REGEX_ONLY_LETTERS, user.user_first_name)
            assert re.search(REGEX_ONLY_LETTERS, user.user_last_name)





