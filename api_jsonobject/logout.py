from jsonobject import *


class DeleteAuthorization(JsonObject):
    Authorization = StringProperty


class BasicErrorResponse(JsonObject):
    general_error = StringProperty
    code = StringProperty
    errors = StringProperty


class ErrorResponse(JsonObject):
    error_response = ObjectProperty(BasicErrorResponse)


class BasicResponse(JsonObject):
    response = "No content"




