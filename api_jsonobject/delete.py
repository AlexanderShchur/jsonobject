from jsonobject import *

URL = 'http://52.207.242.187/auth/logout'


class DeleteAuthorization(JsonObject):
    Authorization = StringProperty


class BasicErrorResponse(JsonObject):
    general_error = StringProperty(name='general_error')
    code = StringProperty(name='code')
    errors = StringProperty(name='errors')


class ErrorResponse(JsonObject):
    error_response = ObjectProperty(BasicErrorResponse)

    def __eq__(self, other):
        return self.error_response.errors == other.errors, self.error_response.code == other.code, self.error_response.general_error == other.general_error

