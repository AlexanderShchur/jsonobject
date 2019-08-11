from jsonobject import *


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
    general_error = StringProperty
    code = StringProperty
    errors = StringProperty


class UserWithSessionResponse(JsonObject):
    user = ObjectProperty(UserResponse)
    session = ObjectProperty(SessionResponse)
