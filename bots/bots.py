import random, string, requests
from config import user_registration, user_get_token


class CreateUser:
    def __init__(self, amount_user: int):
        self.amount_user = amount_user

    def create(self):
        users = []
        for amount in range(self.amount_user):
            user = {}
            username = "".join([random.choice(string.ascii_letters) for _ in range(10)])
            password = "".join([random.choice(string.ascii_letters) for _ in range(10)])
            user["username"] = username
            user["password"] = password
            users.append(user)
        return users


class UserSendDB:
    def __init__(self, url):
        self.url = url

    def user_send(self, data):
        users = []
        for d in data:
            user = {"username": d["username"], "password": d["password"]}
            response = requests.post(self.url, user)
            user_data = response.json()
            user["id"] = user_data["user"]["id"]
            users.append(user)

        return users


class GetUserToken:
    def __init__(self, url):
        self.url = url

    def get_token(self, data):
        tokens = []
        for d in data:
            user = {"username": d["username"], "password": d["password"]}
            response = requests.post(self.url, user)
            user = response.json()
            user["id"] = d["id"]
            tokens.append(user)

        return tokens


class GeneratePost:
    def __init__(self, amount_post):
        self.amount_post = amount_post

    def generate_post(self, users):
        posts = []
        for u in users:
            url = f"http://localhost:8000/api/users/{u['id']}/add_post/"
            access_token = u["access"]

            for amount in range(self.amount_post):
                post = {}
                title = "".join(
                    [random.choice(string.ascii_letters) for _ in range(10)]
                )
                description = "".join(
                    [random.choice(string.ascii_letters) for _ in range(10)]
                )
                post["title"] = title
                post["description"] = description
                posts.append(post)
                response = requests.post(
                    url, post, headers={"Authorization": f"Token {access_token}"}
                )
                data = response.json()
                post["id"] = data["id"]

        return posts


class addLike:
    def add_like(self, users, posts):
        for user in users:
            access_token = user["access"]

            for post in posts:

                urls = [
                    f"http://127.0.0.1:8000/api/posts/{post['id']}/set_like/",
                    f"http://127.0.0.1:8000/api/posts/{post['id']}/set_dislike/",
                ]

                response = requests.post(
                    url=random.choice(urls),
                    headers={"Authorization": f"Token {access_token}"},
                )
                print(response.json())


create_users = CreateUser(3)
user_isFinished = create_users.create()


send_user_db = UserSendDB(user_registration)
users_send = send_user_db.user_send(user_isFinished)


get_user_token = GetUserToken(user_get_token)
users_get_token = get_user_token.get_token(users_send)


create_posts = GeneratePost(5)
post_isFinished = create_posts.generate_post(users_get_token)


add_likes = addLike()
set_like = add_likes.add_like(users_get_token, post_isFinished)
