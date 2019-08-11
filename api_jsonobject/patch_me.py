from jsonobject import *


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
    general_error = StringProperty
    code = StringProperty
    errors = StringProperty



