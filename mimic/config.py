import os
from dotenv import load_dotenv


class Config:
    def __init__(self, **overrides):
        self._db_user = overrides.get("DB_USERNAME", "")
        self._db_pw = overrides.get("DB_PASSWORD", "")
        self._db_host = overrides.get("DB_HOST", "localhost")
        self._db_port = overrides.get("DB_PORT", "27017")

    @classmethod
    def create(cls):
        load_dotenv()
        return cls(**os.environ)

    @property
    def mongodb_uri(self):
        return f"mongodb://{self._db_user}:{self._db_pw}@{self._db_host}:{self._db_port}/mimic?authSource=admin"
