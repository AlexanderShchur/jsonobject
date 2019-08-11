import re
from jsonobject import *


def validate_email(user):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", user):
        raise ValueError(f'Email: {user} is not a valid email!')


class SignUpBody(JsonObject):
    email = StringProperty
    password = StringProperty
    confirm_password = StringProperty


class UserResponse(JsonObject):
    id = IntegerProperty(name='id', required=True)
    email = StringProperty(name='email', required=True, validators=[validate_email])
    is_admin = BooleanProperty(name='is_admin', required=True)
    first_name = StringProperty(name='first_name', required=False)
    last_name = StringProperty(name='last_name', required=False)
    bio = StringProperty(name='bio', required=False)
    created_at = StringProperty(name='created_at', required=True)
    updated_at = StringProperty(name='updated_at', required=True)


class SessionResponse(JsonObject):
    access_token = StringProperty(name='access_token', required=True)
    expires_at = StringProperty(name='expires_at', required=True)


class BasicErrorResponse(JsonObject):
    general_error = StringProperty
    code = StringProperty
    errors = StringProperty


class UserWithSessionResponse(JsonObject):
    user = ObjectProperty(UserResponse)
    session = ObjectProperty(SessionResponse)
