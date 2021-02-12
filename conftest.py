import pytest
from random import randint


@pytest.fixture(scope="function")
def generate_user_id():
    yield randint(1, 10)


@pytest.fixture(scope="function")
def generate_post_id():
    yield randint(1, 100)
