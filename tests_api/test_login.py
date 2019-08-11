import requests

from api_jsonobject.login import *
from constants import BASE_URL, SUCCESS


def test_login_positive_scenario():
    body = {
        'email': "email@example.com",
        'password': 'qwerty1'
    }
    user_to_login = SignInBody(email=body['email'], password=body['password'])
    email = body['email']
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/login', json=user_to_login.to_json(), headers=headers)
    # check status code
    assert SUCCESS == r.status_code
    # check email from response
    assert email == r.json()["user"]["email"]
    if r.status_code == SUCCESS:
        print(UserWithSessionResponse(r.json()))
    else:
        print(BasicErrorResponse(r.json()))


def test_login_negative_scenario():
    body = {
        'email': "email@example.com",
        'password': 'qwerty1qwe',
        'errors': 'invalid credentials',
        'code': 400
    }
    user_to_login = SignInBody(email=body['email'], password=body['password'])
    expected_code = body['code']
    expected_message = body['errors']
    headers = {
        "content-type": "application/json"
    }
    r = requests.post(url=f'{BASE_URL}/auth/login', json=user_to_login.to_json(), headers=headers)
    # check code
    assert expected_code == r.status_code
    # check error message
    assert expected_message == r.json()['errors']
    if r.status_code == SUCCESS:
        print(UserWithSessionResponse(r.json()))
    else:
        print(BasicErrorResponse(r.json()))
