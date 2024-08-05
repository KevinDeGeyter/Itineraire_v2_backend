import os
from fastapi import APIRouter, Request, Body, status, HTTPException
import asyncio
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

routerDataTourisme = APIRouter()




@routerDataTourisme.get("/", response_description="Data Tourisme")
async def hello():
    return {"data": "Hello Data Tourisme"}

