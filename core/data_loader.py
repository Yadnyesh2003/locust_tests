import json

class UserPool:
    users = []
    index = 0

    @classmethod
    def load(cls, path="data/users.json"):
        with open(path) as f:
            cls.users = json.load(f)

    @classmethod
    def get_user(cls):
        user = cls.users[cls.index % len(cls.users)]
        cls.index += 1
        return user
