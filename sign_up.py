import requests
import re
from jsonobject import *

URL = 'http://52.207.242.187/auth/register'
SUCCESS = 200


def validate_email(user):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user):
        raise ValueError(f'Email: {user} is not a valid email!')


class SignUpBody(JsonObject):
    email = StringProperty
    password = StringProperty
    confirm_password = StringProperty


class UserResponse(JsonObject):
    id = IntegerProperty(name='id', required=True)
    email = StringProperty(name='email', required=True)
    is_admin = BooleanProperty(name='is_admin', required=True)
    first_name = StringProperty(name='first_name', required=True)
    last_name = StringProperty(name='last_name', required=True)
    bio = StringProperty(name='bio', required=True)
    created_at = StringProperty(name='created_at', required=True)
    updated_at = StringProperty(name='updated_at', required=True)


class SessionResponse(JsonObject):
    access_token = StringProperty(name='access_token', required=True)
    expires_at = StringProperty(name='expires_at', required=True)


class BasicErrorResponse(JsonObject):
    general_error = StringProperty(name='general_error')
    code = StringProperty(name='code')
    errors = StringProperty(name='errors')


class ErrorResponse(JsonObject):
    error = ObjectProperty(BasicErrorResponse)


class UserWithSessionResponse(JsonObject):
    user = ObjectProperty(UserResponse)
    session = ObjectProperty(SessionResponse)

    def __eq__(self, other):
        return self.user.email == other.email


def sign_up(data):
    print(data.to_json())
    r = requests.post(url=URL, headers={"content-type": "application/json"}, json=data.to_json())
    if r.status_code == SUCCESS:
        return UserWithSessionResponse(r.json())
    else:
        return ErrorResponse(r.json())


user_to_register = SignUpBody(email='te567tl48y7mf6745@example.com', password='qwerty11',
                              comfirm_password='qwerty11')
result = sign_up(user_to_register)
print(result)
