from collections import defaultdict
import json
import os

from fastapi import APIRouter 
from fastapi.requests import Request
from fastapi.responses import JSONResponse

router = APIRouter()

# This is a place holder for what will eventually be getting things from the Database :thinking: MongoDB?
def get_responses(method: str):
  with open(f'{os.getcwd()}/alwayson/.alwayson', 'r') as alwayson_f:
    return json.loads(alwayson_f.read())[method]

# Probably need to persist this outside of the app right now
calls = defaultdict(lambda: 0)

@router.get('/{pathname:path}')
async def get(req: Request, pathname: str) -> JSONResponse:
  path = f'/{pathname}'

  responses = get_responses('get') # retrieve all of the configured get responses
  res = responses.get(path, None)
  if res and isinstance(res, type([])):
    # handle multiple responses
    res_n = res[calls[path]]
    calls[path] += 1
    return JSONResponse(res_n['body'], res_n['status_code'])
  elif res:
    # Handle the case of a singlse response
    return JSONResponse(res['body'], res['status_code'])
  
  # This is a bad request instead of 404 b/c the endpoint was found but the request has not
  # been configured ahead of time.
  return JSONResponse({ 'message': f'{path} has not been configured with a response'}, 400)
