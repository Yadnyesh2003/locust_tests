import yaml

class Config:
    data = {}

    @classmethod
    def load(cls):
        with open("config.yaml") as f:
            cls.data = yaml.safe_load(f)
