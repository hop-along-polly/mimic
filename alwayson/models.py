from typing import Annotated, Any, Dict, List, Union

from pydantic import BaseModel
import jwt

# TODO This needs to become a setting specifically for the
# tenant
SECRET = "always-on-secret-key"


class JWTEncodeable:
    def encode(self) -> str:
        # TODO I may just be able to use this as a self.__dict__ or something and it works for everything
        # TODO I may also want this to take in a SECRET and org/tenant...actually that will be encoded
        # by the SECRET since that will be specific to each org/tenant.
        pass


class AlwaysOnResponse(BaseModel):
    status_code: (
        int  # TODO could probably further restruct this to valid HTTP status codes.
    )
    body: Union[Dict[str, Any], List[Dict]]

    # TODO This is 100% a misplaced responsibility since it's decoding a list of AlwaysOnResponses
    # and not just a single one.
    # I think the solution is creating a Encodeable class that has default encode/decode methods
    # and each of these classes can overwrite those as needed.
    @classmethod
    def decode_responses(cls, res: str):
        decoded = jwt.decode(res, SECRET, algorithms=["HS256"])["responses"]
        return [cls(**r) for r in decoded]

    # TODO This is 100% a misplaced responsibility since it's decoding a list of AlwaysOnResponses
    # and not just a single one.
    # I think the solution is creating a Encodeable class that has default encode/decode methods
    # and each of these classes can overwrite those as needed.
    @classmethod
    def decode_responses(cls, res: str):
        decoded = jwt.decode(res, SECRET, algorithms=["HS256"])["responses"]
        return [cls(**r) for r in decoded]


class AlwaysOnRequest(BaseModel, JWTEncodeable):
    method: str  # TODO make this an enum
    url: str  # TODO add some regex validation?

    def encode(self):
        return jwt.encode(self.__dict__, SECRET)


# Handles the AlwaysON manifest
class ManifestEntry(BaseModel):
    request: AlwaysOnRequest
    responses: Union[AlwaysOnResponse, List[AlwaysOnResponse]]

    @classmethod
    def decode_and_create(cls, req: str, res: str):
        request = jwt.decode(req, SECRET, algorithms=["HS256"])

        decoded_res = jwt.decode(res, SECRET, algorithms=["HS256"])["responses"]
        responses = [AlwaysOnResponse(**r) for r in decoded_res]

        return cls(request=request, responses=responses)

    def encoded_request(self):
        return jwt.encode(self.request.__dict__, SECRET)

    def encoded_responses(self):
        payload = {"responses": [r.__dict__ for r in self.responses]}
        return jwt.encode(payload, SECRET)


# TODO figure out if I could make this class...may not be possible.
Manifest = Annotated[List[ManifestEntry], Any]
