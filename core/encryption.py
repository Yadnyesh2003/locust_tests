from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64
import os
from core.config_loader import Config

Config.load()
SECRET_KEY = Config.data["SECRET_KEY"]


def encrypt_password(plain_password: str) -> str:
    iv = os.urandom(16)

    ctr = Counter.new(
        128,
        initial_value=int.from_bytes(iv, byteorder="big")
    )

    cipher = AES.new(
        SECRET_KEY.encode("utf-8"),
        AES.MODE_CTR,
        counter=ctr
    )

    encrypted = cipher.encrypt(plain_password.encode("utf-8"))

    return base64.b64encode(iv + encrypted).decode("utf-8")
