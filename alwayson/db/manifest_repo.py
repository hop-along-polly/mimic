from typing import List

from motor.motor_asyncio import AsyncIOMotorClient

from alwayson.config import Config
from alwayson.models import ManifestEntry


# TODO this probably should be able to select a DB or collection that's
# specific for the customer.
class ManifestRepo:
  def __init__(self, client):
    self._collection = client['always-on']['manifests']

  @classmethod
  def create(cls, cfg: Config):
    return cls(AsyncIOMotorClient(cfg.mongodb_uri))

  # TODO Ensure this raises and error if the write fails.
  async def upsert(self, entry: ManifestEntry) -> None:
    req_jwt = entry.encoded_request() # TODO Probably need to pass the Org specific secret here
    res_jwt = entry.encoded_responses() # TODO Probably need to pass the Org specific secret here

    query = { 'request': req_jwt }
    update = { '$set': { 'request': req_jwt, 'responses': res_jwt } }

    await self._collection.update_one(query, update, upsert=True)
