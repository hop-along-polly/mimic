from typing import Annotated, Dict

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from testerozza.config import Config
from testerozza.db.client import DbClient

router = APIRouter()


def get_db_client():
    cfg = Config.create()
    return DbClient.create(cfg)


@router.get("/status")
async def status(db: Annotated[Dict, Depends(get_db_client)]):
    db_health = await db.health()
    return JSONResponse({"api": "online", "db": db_health}, 200)
