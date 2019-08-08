from jsonobject import *

URL = 'http://52.207.242.187/users/me'


class EditProfileBody(JsonObject):
    first_name = StringProperty
    last_name = StringProperty
    bio = StringProperty


class Authorization(JsonObject):
    Authorization = StringProperty


class UserBasicResponse(JsonObject):
    id = IntegerProperty(name='id', required=True)
    email = StringProperty(name='email', required=True)
    is_admin = BooleanProperty(name='is_admin', required=True)
    first_name = StringProperty(name='first_name', required=True)
    last_name = StringProperty(name='last_name', required=True)
    bio = StringProperty(name='bio', required=True)
    created_at = StringProperty(name='created_at', required=True)
    updated_at = StringProperty(name='updated_at', required=True)


class BasicErrorResponse(JsonObject):
    general_error = StringProperty(name='general_error')
    code = StringProperty(name='code')
    errors = StringProperty(name='errors')


class ErrorResponse(JsonObject):
    error_response = ObjectProperty(BasicErrorResponse)

    def __eq__(self, other):
        return self.error_response.errors == other.errors, self.error_response.code == other.code, self.error_response.general_error == other.general_error


class UserResponse(JsonObject):
    user_basic = ObjectProperty(UserBasicResponse)

    def __eq__(self, other):
        return self.user_basic.email == other.email
