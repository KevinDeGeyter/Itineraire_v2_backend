import os
from fastapi import APIRouter, Request, Body, status, HTTPException
import asyncio
import logging
import json
from geopy.distance import geodesic
from neo4j import GraphDatabase
from sklearn.cluster import KMeans
import psycopg2

# logger = logging.getLogger('uvicorn.error')
# logger.setLevel(logging.DEBUG)

routerDataTourisme = APIRouter()

# Configurer le format de journalisation
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Créer un logger
logger = logging.getLogger(__name__)


@routerDataTourisme.get("/", response_description="Data Tourisme")
async def hello():
    return {"data": "Hello Data Tourisme"}


# Fonction pour filtrer les points d'intérêt dans un rayon donné autour d'une position
def filter_pois(position, pois, radius_km):
    list_pois = []
    for poi in pois:
        poi_latitude, poi_longitude = float(poi[1]), float(poi[2])
        if -90 <= poi_latitude <= 90 and -180 <= poi_longitude <= 180:
            poi_position = (poi_latitude, poi_longitude)
            if geodesic(position, poi_position).kilometers <= radius_km:
                list_pois.append(poi)
        else:
            print("Coordonnées incorrectes")
    return list_pois


@routerDataTourisme.post("/graph", response_description="Data Tourisme")
async def create_graph_neo4j(data: dict = Body(...)):
    # await asyncio.sleep(5)
    # received_data = {"result": data}
    logger.debug("create_graph %s", json.dumps(data, indent=4))

    return {"status": "OK", "data": data}
