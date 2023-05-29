import pytest
from api.entities.user import User


@pytest.fixture()
def generate_user():
    return User.generate_random()


@pytest.fixture()
def status_code_ok():
    return 200


@pytest.fixture()
def status_code_not_found():
    return 404

@pytest.fixture()
def check_git_source():
    return 'OK'
