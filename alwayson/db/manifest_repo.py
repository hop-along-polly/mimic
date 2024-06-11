from typing import List, Union

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import ReturnDocument

from alwayson.config import Config
from alwayson.models import AlwaysOnResponse, ManifestEntry, AlwaysOnRequest


# TODO this probably should be able to select a DB or collection that's
# specific for the customer.
class ManifestRepo:
    def __init__(self, client):
        self._collection = client["always-on"]["manifests"]

    @classmethod
    def create(cls, cfg: Config):
        return cls(AsyncIOMotorClient(cfg.mongodb_uri))

    # TODO Ensure this raises and error if the write fails.
    async def upsert(self, entry: ManifestEntry) -> None:
        req_jwt = (
            entry.encoded_request()
        )  # TODO Probably need to pass the Org specific secret here
        res_jwt = (
            entry.encoded_responses()
        )  # TODO Probably need to pass the Org specific secret here

        query = {"request": req_jwt}
        update = {"$set": {"request": req_jwt, "responses": res_jwt, "called": 0}}

        await self._collection.update_one(query, update, upsert=True)

    async def get_responses(self, request: AlwaysOnRequest):
        req_jwt = request.encode()

        query = {"request": req_jwt}
        update = {"$inc": {"called": 1}}

        doc = await self._collection.find_one_and_update(
            query, update, return_doc=ReturnDocument.AFTER
        )

        if not doc:
            return doc, -1

        responses = AlwaysOnResponse.decode_responses(doc["responses"])
        return responses, doc["called"]
