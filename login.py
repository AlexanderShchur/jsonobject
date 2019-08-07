from jsonobject import *
import requests

URL = 'http://52.207.242.187/auth/login'
SUCCESS = 200


class SignInBody(JsonObject):
    email = StringProperty
    password = StringProperty


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

    def __eq__(self, other):
        return self.error.errors == other.errors


class UserWithSessionResponse(JsonObject):
    user = ObjectProperty(UserResponse)
    session = ObjectProperty(SessionResponse)

    def __eq__(self, other):
        return self.user.email == other.email, self.session.access_token == other.access_token


def login(data):
    r = requests.post(url=URL, headers={"content-type": "application/json"}, json=data.to_json())
    if r.status_code == SUCCESS:
        return UserWithSessionResponse(r.json())
    else:
        return ErrorResponse(r.json())


user_to_login = SignInBody(email='email@example.com', password='qwerty1')
result = login(user_to_login)
print(result)
