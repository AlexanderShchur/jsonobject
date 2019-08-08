import pytest
import requests
import json
from pytest.constants import *


@pytest.fixture(scope='function')
def logged_user():
    default_user = {'email': 'email@example.com', 'password': 'qwerty1'}
    headers = {
        "content-type": "application/json"
    }
    login = requests.post(url=f'{BASE_URL}/auth/login', data=json.dumps(default_user), headers=headers)
    yield login.json()
    body = json.loads(login.content)
    token = body['session']['access_token']
    authorization_header = {
        "authorization": token
    }
    logout = requests.delete(url=f'{BASE_URL}/auth/logout', headers=authorization_header)


@pytest.fixture(scope='function')
def logged_user(request):
    default_user = {'email': 'email@example.com', 'password': 'qwerty1'}
    headers = {
        "content-type": "application/json"
    }
    login = requests.post(url=f'{BASE_URL}/auth/login', data=json.dumps(default_user), headers=headers)

    def fin():
        body = json.loads(login.content)
        token = body['session']['access_token']
        authorization_header = {
            "authorization": token
        }
        requests.delete(url=f'{BASE_URL}/auth/logout', headers=authorization_header)

    request.addfinalizer(fin)
    return login.json()


def test_get_my_profile(logged_user):
    r = requests.get(url=f'{BASE_URL}/users/me', headers={"Authorization": logged_user["session"]["access_token"]})
    assert SUCCESS == r.status_code
    assert logged_user["user"]["id"] == r.json()["id"]

# Задача
# Написать код фикстуры logged_user. Должна авторизовать юзера, вернуть респонс в тест, выполнить логаут после теста
# Фикстуру написать в двух вариантах с использованием addfinalizer и через yield
