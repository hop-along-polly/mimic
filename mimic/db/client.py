from motor.motor_asyncio import AsyncIOMotorClient


class DbClient:
    def __init__(self, client):
        self._client = client

    @classmethod
    def create(cls, config):
        return cls(AsyncIOMotorClient(config.mongodb_uri))

    async def health(self):
        try:
            await self._client["mimic"].command("ping")
        except Exception as e:
            print(e)
            return "offline"
        return "online"
