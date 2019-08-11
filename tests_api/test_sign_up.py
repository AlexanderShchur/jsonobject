import random
import time
import pytest
import requests

from api_jsonobject.sign_up import *
from constants import BASE_URL, SUCCESSFULLY_CREATED

positive_test_data = [
    {
        'email': f"email{int(time.time())}@example.com",
        'password': 'qwerty1',
        'confirm_password': 'qwerty1'
    },
    {
        'email': f"email{random.randint(10000, 100000)}@example.com",
        'password': 'qwerty1',
        'confirm_password': 'qwerty1'
    }
]

negative_test_data = [
    {
        # email already exists
        'email': 'email@example.com',
        'password': 'qwerty1',
        'confirm_password': 'qwerty1',
        'code': 422,
        'errors': 'user with such email already exist'
    },
    {
        # password should be consists more than 6 symbols
        'email': 'z12345@example.com',
        'password': 'qwerty',
        'confirm_password': 'qwerty',
        'code': 400,
        'errors': {'password': ['Password should have 1 letter and 1 digit. Password cannot contain spaces.']}
    },
    {
        # password and confirm password does not match
        'email': 'z12345@example.com',
        'password': 'qwerty1',
        'confirm_password': 'qwerty12',
        'code': 400,
        'errors': {'confirm_password': ['Passwords do not match.']}
    },
    {
        # password should be contain at least 1 digit
        'email': 'z12345@example.com',
        'password': 'qwertyu',
        'confirm_password': 'qwertyu',
        'code': 400,
        'errors': {'password': ['Password should have 1 letter and 1 digit. Password cannot contain spaces.']}
    }
]


@pytest.fixture(params=positive_test_data)
def positive_fixture(request):
    return request.param


@pytest.fixture(params=negative_test_data)
def negative_fixture(request):
    return request.param


def test_sign_up_positive_scenario(positive_fixture):
    body = {
        "email": positive_fixture['email'],
        "password": positive_fixture['password'],
        "confirm_password": positive_fixture['confirm_password']
    }
    user_to_register = SignUpBody(email=body['email'], password=body['password'], confirm_password=body['confirm_password'])
    email = positive_fixture['email']
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', json=user_to_register.to_json(), headers=headers)
    # check status code
    assert SUCCESSFULLY_CREATED == r.status_code
    # check email from response
    assert email == r.json()["user"]["email"]
    if r.status_code == SUCCESSFULLY_CREATED:
        print(UserWithSessionResponse(r.json()))
    else:
        print(BasicErrorResponse(r.json()))


def test_sign_up_negative_scenario(negative_fixture):
    body = {
        "email": negative_fixture['email'],
        "password": negative_fixture['password'],
        "confirm_password": negative_fixture["confirm_password"]
    }
    user_to_register = SignUpBody(email=body['email'], password=body['password'], confirm_password=body['confirm_password'])
    expected_code = negative_fixture['code']
    expected_message = negative_fixture['errors']
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', json=user_to_register.to_json(), headers=headers)
    # check code
    assert expected_code == r.status_code
    # check error message
    assert expected_message == r.json()['errors']
    if r.status_code == SUCCESSFULLY_CREATED:
        print(UserWithSessionResponse(r.json()))
    else:
        print(BasicErrorResponse(r.json()))
