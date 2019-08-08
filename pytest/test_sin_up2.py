import pytest
import time
import requests
import json
import random

from pytest.constants import BASE_URL, SUCCESSFULLY_CREATED, UNPROCESSABLE_ENTITY, USER_ALREADY_EXIST_ERROR, BAD_REQUEST

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
        'confirm_password': 'qwerty1'
    },
    {
        # password should be consists more than 6 symbols
        'email': 'z12345@example.com',
        'password': 'qwerty1',
        'confirm_password': 'qwerty1'
    },
    {
        # password and confirm password does not match
        'email': 'z12345@example.com',
        'password': 'qwerty1',
        'confirm_password': 'qwerty1'
    },
    {
        # password should be contain at least 1 digit
        'email': 'z12345@example.com',
        'password': 'qwerty1',
        'confirm_password': 'qwerty1'
    }
]


@pytest.mark.parametrize('body_test', positive_test_data)
def test_sign_up_positive_scenario(body_test):
    email = body_test['email']
    body = {
        "email": email,
        "password": body_test['password'],
        "confirm_password": body_test['confirm_password']
    }
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', data=json.dumps(body), headers=headers)
    # check status code
    assert SUCCESSFULLY_CREATED == r.status_code
    # check email from response
    assert email == r.json()["user"]["email"]


@pytest.mark.parametrize('body_test', negative_test_data)
def test_sign_up_negative_scenario(body_test):
    body = {
        "email": body_test['email'],
        "password": body_test['password'],
        "confirm_password": body_test['confirm_password']
    }
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/register', data=json.dumps(body), headers=headers)
    if r.status_code == 422:
        assert UNPROCESSABLE_ENTITY == r.status_code
    # check expected error
        assert USER_ALREADY_EXIST_ERROR == r.json()['errors']
    elif r.status_code == 400:
        assert BAD_REQUEST == r.status_code
    else:
        assert SUCCESSFULLY_CREATED == r.status_code

#  Задача
#  Расширить функциональность тестов параметризоваными фикстурами. Написать 2 варианта тестовых данных для первого теста
#  и 4 варианта для второго. Фикстуры должны отдавать в тест данные и ожидаемый результат. Потом изменить код тестов,
#  Так чтобы они заработали
#
