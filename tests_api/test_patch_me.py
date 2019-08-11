import json

import pytest
import requests

from api_jsonobject.patch_me import *
from api_jsonobject.login import *

from constants import SUCCESS, BASE_URL, UNAUTHORIZED, BAD_REQUEST


@pytest.fixture(scope='function')
def logged_user():
    body = {
        'email': "email@example.com",
        'password': 'qwerty1'
    }
    user_to_login = SignInBody(email=body['email'], password=body['password'])
    headers = {
        "content-type": "application/json"
    }
    login = requests.post(url=f'{BASE_URL}/auth/login', json=user_to_login.to_json(), headers=headers)
    body = json.loads(login.content)
    token = body['session']['access_token']
    return token


def test_positive_patch_me(logged_user):
    change_info = EditProfileBody(first_name="John", last_name="Targarien", bio="The king of all")
    r = requests.patch(url=f'{BASE_URL}/users/me',
                       headers={"Authorization": logged_user, "content-type": "application/json"},
                       json=change_info.to_json())
    assert SUCCESS == r.status_code
    if r.status_code == SUCCESS:
        print(UserBasicResponse(r.json()))
    else:
        print(BasicErrorResponse(r.json()))


def test_negative_patch_me(logged_user):
    change_info = EditProfileBody(first_name="John", last_name="Targarien", bio="The king of all")
    r = requests.patch(url=f'{BASE_URL}/users/me',
                       headers={"Authorization": logged_user+'1', "content-type": "application/json"},
                       json=change_info.to_json())
    assert UNAUTHORIZED == r.status_code or BAD_REQUEST == r.status_code
    if r.status_code == SUCCESS:
        print(UserBasicResponse(r.json()))
    else:
        print(BasicErrorResponse(r.json()))
