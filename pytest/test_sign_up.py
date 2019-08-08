import pytest
import time
import requests
import json
import random
import logging

from pytest.constants import BASE_URL, SUCCESSFULLY_CREATED

logging.basicConfig(filename='test_app.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(name)s - %('
                                                                                      'levelname)s - %(message)s')

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
    logging.info("Return request body with valid data to the positive test")
    return request.param


@pytest.fixture(params=negative_test_data)
def negative_fixture(request):
    logging.info("Return request body with invalid data to the negative test")
    return request.param


def test_sign_up_positive_scenario(positive_fixture):
    body = {
        "email": positive_fixture['email'],
        "password": positive_fixture['password'],
        "confirm_password": positive_fixture['confirm_password']
    }
    email = positive_fixture['email']
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', data=json.dumps(body), headers=headers)
    # check status code
    logging.info("Check status code")
    assert SUCCESSFULLY_CREATED == r.status_code
    # check email from response
    logging.info("Email verification")
    assert email == r.json()["user"]["email"]


def test_sign_up_negative_scenario(negative_fixture):
    body = {
        "email": negative_fixture['email'],
        "password": negative_fixture['password'],
        "confirm_password": negative_fixture["confirm_password"]
    }
    expected_code = negative_fixture['code']
    expected_message = negative_fixture['errors']
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', data=json.dumps(body), headers=headers)
    # check code
    logging.info("Check status code")
    assert expected_code == r.status_code
    # check error message
    logging.info("Check the expected error message")
    assert expected_message == r.json()['errors']
#  Задача
#  Расширить функциональность тестов параметризоваными фикстурами. Написать 2 варианта тестовых данных для первого теста
#  и 4 варианта для второго. Фикстуры должны отдавать в тест данные и ожидаемый результат. Потом изменить код тестов,
#  Так чтобы они заработали
#
