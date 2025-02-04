from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from testerozza.controllers.injectors import inject_manifest_repo
from testerozza.models import TesterozzaRequest


router = APIRouter()


@router.get("/{pathname:path}")
async def get(
    req: Request,
    pathname: str,
    manifests: Annotated[dict, Depends(inject_manifest_repo)],
) -> JSONResponse:
    request = TesterozzaRequest(
        method=req.method,  # Could honestly hardcode this but I'm thinking of creating a middleware that does this for us.
        url=str(
            req.url
        ),  # TODO Consider only using a path and not the full url i.e `/health` instead of `http://localhost:/health`
    )

    responses, calls = await manifests.get_responses(request)

    if not responses or len(responses) <= calls:
        return JSONResponse(
            {"message": f"/{pathname} has not been configured with a response"}, 400
        )

    res = responses[calls]
    return JSONResponse(res.body, res.status_code)
