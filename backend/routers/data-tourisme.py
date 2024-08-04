import os
from fastapi import APIRouter, Request, Body, status, HTTPException
import requests
import logging

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

router = APIRouter()

@router.get("/", response_description="Data Tourisme")
async def hello():
    return {"data":"Hello Data Tourisme"}


