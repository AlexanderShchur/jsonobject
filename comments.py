# URL = 'http://52.207.242.187/auth/register'
# SUCCESS = 201
#
# positive_test_data = {
#     'email': f"email{int(time.time())}@example.com",
#     'password': 'qwerty1',
#     'confirm_password': 'qwerty1'
# }

# def sign_up(data):
#     print(data.to_json())
#     r = requests.post(url=URL, headers={"content-type": "application/json"}, json=data.to_json())
#     if r.status_code == SUCCESS:
#         return UserWithSessionResponse(r.json())
#     else:
#         return BasicErrorResponse(r.json())


# def test_sign_up():
#     user_to_register = SignUpBody(email=positive_test_data['email'], password=positive_test_data['password'],
#                                   confirm_password=positive_test_data['confirm_password'])
#     result = sign_up(user_to_register)
#     print(result)


# def login(data):
#     r = requests.post(url=URL, headers={"content-type": "application/json"}, json=data.to_json())
#     if r.status_code == SUCCESS:
#         return UserWithSessionResponse(r.json())
#     else:
#         return BasicErrorResponse(r.json())
#
#
# user_to_login = SignInBody(email='1email@example.com', password='qwerty122')
# result = login(user_to_login)
# print(result)

# import requests

# URL = 'http://52.207.242.187/auth/login'
# SUCCESS = 200

# def test_get_me(data):
#     r = requests.get(url=URL, headers={"Authorization": data, "content-type": "application/json"})
#     if r.status_code == 200:
#         return UserBasicResponse(r.json())
#     else:
#         return BasicErrorResponse(r.json())
#
#
# info = logged_user()
# print(info)
# result = test_get_me(info)
# print(result)

# URL = 'http://52.207.242.187/users/me'
#
#
# def logged_user():
#     default_user = {'email': 'email@example.com', 'password': 'qwerty1'}
#     headers = {
#         "content-type": "application/json"
#     }
#     login = requests.post(url="http://52.207.242.187/auth/login", json=default_user, headers=headers)
#     body = json.loads(login.content)
#     token = body['session']['access_token']
#     return token

# def test_delete(token):
#     r = requests.delete(url=URL, headers={"Authorization": token, "content-type": "application/json"})
#     if r.status_code == 204:
#         return BasicResponse()
#     else:
#         return BasicErrorResponse(r.json())
#
#
# info = logged_user()
# print(info)
# result = test_delete(info)
# print(result)
# URL = 'http://52.207.242.187/auth/logout'
#
#
# def logged_user():
#     default_user = {'email': 'email@example.com', 'password': 'qwerty1'}
#     headers = {
#         "content-type": "application/json"
#     }
#     login = requests.post(url="http://52.207.242.187/auth/login", json=default_user, headers=headers)
#     body = json.loads(login.content)
#     token = body['session']['access_token']
#     return token

# def test_patch_me(token, data):
# #     r = requests.patch(url=URL, headers={"Authorization": token, "content-type": "application/json"}, json=data.to_json())
# #     if r.status_code == 200:
# #         return UserBasicResponse(r.json())
# #     else:
# #         return BasicErrorResponse(r.json())
# #
# #
# # edit_info = EditProfileBody(first_name="Danny", last_name="Targarien", bio="The king of all")
# # info = logged_user()
# # print(info)
# # result = test_patch_me(info, edit_info)
# # print(result)

# URL = 'http://52.207.242.187/users/me'
#
#
# def logged_user():
#     default_user = {'email': 'email@example.com', 'password': 'qwerty1'}
#     headers = {
#         "content-type": "application/json"
#     }
#     login = requests.post(url="http://52.207.242.187/auth/login", json=default_user, headers=headers)
#     body = json.loads(login.content)
#     token = body['session']['access_token']
#     return token
