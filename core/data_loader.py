import csv

class UserPool:
    users = []
    index = 0

    @classmethod
    def load(cls, path="data/users.csv"):
        with open(path) as f:
            cls.users = list(csv.DictReader(f))

    @classmethod
    def get_user(cls):
        user = cls.users[cls.index % len(cls.users)]
        cls.index += 1
        return user
