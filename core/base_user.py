from locust import HttpUser
from core.data_loader import UserPool

UserPool.load()

class BaseUser(HttpUser):

    abstract = True

    def on_start(self):
        user = UserPool.get_user()

        self.user_id = user["user_id"]
        self.username = user["username"]
        self.token = user["token"]