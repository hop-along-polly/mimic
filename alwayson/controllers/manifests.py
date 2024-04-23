from typing import Dict, Any, Union, List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel


# Handles the specific response for a URL in a AlwaysON Manifest
# {
#   "status_code": <int>,
#   "body": <JSONObject>
# }
# OR
# {
#   "status_code": <int>,
#   "body": <JSONList<JSONObject>>
# }
# TODO Support Files being returned
class AlwaysOnResponse(BaseModel):
  status_code: int # TODO could probably further restruct this to valid HTTP status codes.
  body: Union[Dict[str, Any], List[Dict]]


# Handles the AlwaysON manifest
class Manifest(BaseModel):
  # TODO add post, put, patch, and delete
  get: Dict[str, Union[AlwaysOnResponse, List[AlwaysOnResponse]]]


router = APIRouter(prefix='/manifests')


# TODO Allow this to handle uploading a file instead of posting a JSON body
@router.post('/')
async def upload(manifest: Manifest) -> JSONResponse:
  print('Manifest:', manifest)
  print('Multi-health:', manifest.get['/multi-health'])

  return JSONResponse({}, 201)
