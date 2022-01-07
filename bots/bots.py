import random, string, requests
from config import user_registration, user_get_token


class CreateUser:
    
    def __init__(self, amount_user: int):
        self.amount_user = amount_user

    def create(self):
        users = []
        for amount in range(self.amount_user):
            user = {}
            username = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
            password = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
            user['username'] = username
            user['password'] = password
            users.append(user)
        return users

class UserSendDB:

    def __init__(self, url):
        self.url = url

    def user_send(self, data):
        users = []
        for d in data:
            user = {"username": d['username'], "password": d['password']}
            response = requests.post(self.url, user)
            data = response.json()
            print(data['user']['id'])
        #     users.append(response.content)
        # print(users)
        return data, users

# class GetUserToken:

#     def __init__(self, url):
#         self.url = url

#     def get_token(self, data):
#         tokens = []
#         for d in data:
#             user = {"username": d['username'], "password": d['password']}
#             response = requests.post(self.url, user)
#             tokens.append(response.content)
#         return tokens



create_users = CreateUser(2)
user_isFinished = create_users.create()


send_user_db = UserSendDB(user_registration)
users_send = send_user_db.user_send(user_isFinished)

# get_user_token = GetUserToken(user_get_token)
# users_get_token = get_user_token.get_token(users_send)
# print(users_get_token)
