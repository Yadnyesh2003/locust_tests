# from locust import HttpUser, between
# from core.auth import login
# from core.data_loader import UserPool
# from core.config_loader import Config

# Config.load()
# UserPool.load()

# class BaseUser(HttpUser):

#     wait_time = between(
#         Config.data["wait_min"],
#         Config.data["wait_max"]
#     )

#     def on_start(self):

#         creds = UserPool.get_user()

#         self.user_id = creds["user_id"]
#         self.user_name = creds["user_name"]

#         self.cookies = login(self, creds)

#     def api(self, method, url, **kwargs):

#         kwargs["cookies"] = self.cookies

#         headers = kwargs.setdefault("headers", {})

#         headers.update({
#             "Content-Type": "application/json",
#             "Accept": "application/json",
#             "user-id": self.user_id,
#             "user-name": self.user_name
#         })

#         return self.client.request(method, url, **kwargs)


from locust import HttpUser
from core.helpers import random_user
from core.encryption import encrypt_password

# SECRET_KEY = "your-secret-key-1234567890abcdef"

class BaseUser(HttpUser):

    abstract = True

    def on_start(self):
        user = random_user()

        self.user_id = user["user_id"]
        self.user_name = user["user_name"]

        payload = {
            "email": user["email"],
            "password": encrypt_password(user["password"])
        }

        res = self.client.post("/api/user/login/", json=payload)

        if res.status_code != 200:
            res.failure("Login failed")

        self.cookies = res.cookies
