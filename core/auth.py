from core.encryption import encrypt_password

def login(user, creds):

    payload = {
        "email": creds["email"],
        "password": encrypt_password(creds["password"])
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    res = user.client.post("/api/user/login/", json=payload, headers=headers)

    if res.status_code != 200:
        raise Exception(f"Login failed for {creds['email']}")

    return res.cookies
