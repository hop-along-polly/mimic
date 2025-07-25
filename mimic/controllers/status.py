from typing import Annotated, Dict

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from mimic.config import Config
from mimic.db.client import DbClient

router = APIRouter()


def get_db_client():
    cfg = Config.create()
    return DbClient.create(cfg)


@router.get('/liveness')
async def live():
    return JSONResponse({ "api": "online" })


@router.get('/readiness')
async def ready(db: Annotated[Dict, Depends(get_db_client)]):
    db_health = await db.health()
    return JSONResponse({ "api": "online", "db": db_health }, 200)
