from typing import Annotated, Any, Dict, List, Union

from pydantic import BaseModel
import jwt

# TODO This needs to become a setting specifically for the 
# tenant
SECRET = 'always-on-secret-key'


# TODO I Should have an AlwaysOn Request/Response Exchange
# object where the encode and decode stuff can be abstracted
class AlwaysOnResponse(BaseModel):
  status_code: int # TODO could probably further restruct this to valid HTTP status codes.
  body: Union[Dict[str, Any], List[Dict]]


class AlwaysOnRequest(BaseModel):
  method: str  # TODO make this an enum
  url: str     # TODO add some regex validation?


# Handles the AlwaysON manifest
class ManifestEntry(BaseModel):
  request: AlwaysOnRequest
  responses: Union[AlwaysOnResponse, List[AlwaysOnResponse]]

  @classmethod
  def decode_and_create(cls, req: str, res: str):
    request = jwt.decode(req, SECRET, algorithms=['HS256'])

    decoded_res = jwt.decode(res, SECRET, algorithms=['HS256'])['responses']
    responses = [ AlwaysOnResponse(**r) for r in decoded_res ]

    return cls(request=request, responses=responses)


  def encoded_request(self):
    return jwt.encode(self.request.__dict__, SECRET)

  def encoded_responses(self):
    payload = {
      'responses': [ r.__dict__ for r in self.responses ]
    }
    return jwt.encode(payload, SECRET)

# TODO figure out if I could make this class...may not be possible.
Manifest = Annotated[List[ManifestEntry], Any]
