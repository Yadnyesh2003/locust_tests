import json
import csv
from core.encryption import encrypt_password
import requests
from core.config_loader import Config

Config.load()

CSV_FILE = "data/userData.csv"
USERS_FILE = "data/users.json"
HOST = Config.data["HOST"]
SECRET_KEY = Config.data["SECRET_KEY"]

def main():
    with open(CSV_FILE) as f:
        reader = csv.DictReader(f)
        users = [dict(row) for row in reader]

    admin = users[0]
    test_users = users[1:]

    # Admin login
    payload = {
        "email": admin["email"],
        "password": encrypt_password(admin["password"])
    }
    r = requests.post(f"{HOST}/api/user/login/", json=payload)
    r.raise_for_status()
    cookies = r.cookies

    # Fetch all users
    r = requests.get(f"{HOST}/api/user/all-users/", cookies=cookies)
    r.raise_for_status()
    all_users = r.json()
    email_to_id = {u["email"]: u["id"] for u in all_users}
    email_to_name = {u["email"]: u.get("name", u["email"]) for u in all_users}

    # Login CSV users one by one, respecting rate limits
    users_data = []
    for user in test_users:
        email = user["email"]
        password = encrypt_password(user["password"])
        r = requests.post(f"{HOST}/api/user/login/", json={"email": email, "password": password})
        if r.status_code == 200:
            token = r.cookies.get("access_token") or r.json().get("token")
            users_data.append({
                "email": email,
                "user_id": email_to_id[email],
                "username": email_to_name[email],
                "token": token
            })
            print(f"✅ {email} logged in")
        else:
            print(f"❌ {email} login failed: {r.status_code} {r.text}")
    
    with open(USERS_FILE, "w") as f:
        json.dump(users_data, f, indent=2)

if __name__ == "__main__":
    main()
