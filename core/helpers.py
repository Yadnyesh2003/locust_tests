import csv
import random

def load_users(path="data/users.csv"):
    with open(path) as f:
        return list(csv.DictReader(f))

USERS = load_users()

def random_user():
    return random.choice(USERS)
