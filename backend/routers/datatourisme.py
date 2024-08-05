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


@routerDataTourisme.post("/graph", response_description="Data Tourisme")
async def create_graph(data: dict = Body(...)):
    await asyncio.sleep(30)
    return {
        "latitude": data.latitude,
        "longitude": data.longitude,
        "poi_types": data.poi_types,
        "radius": data.radius
    }
