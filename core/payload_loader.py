import json
import random
from pathlib import Path

BASE = Path("payloads")

class PayloadManager:

    cache = {}

    @classmethod
    def random_payload(cls, app, api):

        key = f"{app}/{api}"

        if key not in cls.cache:
            with open(BASE / app / f"{api}.json") as f:
                cls.cache[key] = json.load(f)

        return random.choice(cls.cache[key])
