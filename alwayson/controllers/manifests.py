from typing import Annotated, Dict

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from alwayson.config import Config
from alwayson.models import Manifest
from alwayson.db.manifest_repo import ManifestRepo


router = APIRouter(prefix='/manifests')


def get_manifest_repo():
  cfg = Config.create()
  # TODO In middleware we would need to figure out how to get the
  # org name from the JWT and then pass it here so it selects the
  # correct customer DB
  return ManifestRepo.create(cfg)

# TODO Allow this to handle uploading a file instead of posting a JSON body
# TODO Consider using a transaction so only a fully successful upload works....ah but maybe this doesn't matter with session
@router.post('')
async def upload(manifest: Manifest, manifests: Annotated[dict, Depends(get_manifest_repo)]) -> JSONResponse:
  # TODO could probably get away with an upsert many on this.
  failed = []
  for entry in manifest:
    try:
      await manifests.upsert(entry)
    except Exception as e:
      failed.append(entry.json())
      print('Error occurred during an upsert', e)

  if len(failed) > 0:
    return JSONResponse( { 'failed': failed }, 400)

  return JSONResponse({}, 201)
