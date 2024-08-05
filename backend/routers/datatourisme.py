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
    await asyncio.sleep(5)
    received_data = {"result": data}
    logger.debug("create_graph %s", json.dumps(data, indent=4))

    # Connexion à la base de données PostgreSQL
    conn = psycopg2.connect(
        host="188.166.105.53",
        port="65001",
        database="postgres",
        user="postgres",
        password="LearnPostgreSQL"
    )
    cursor = conn.cursor()

    # Requête SQL pour récupérer les points d'intérêt correspondant aux types spécifiés
    poi_types_condition = " OR ".join([f"tp.type = '{poi_type}'" for poi_type in received_data.result.poi_types])
    sql_query = (
        "SELECT dt.label_fr, dt.latitude, dt.longitude, tp.type "
        "FROM datatourisme dt "
        "JOIN liaison_datatourisme_types_de_poi ldtp ON dt.id = ldtp.id_datatourisme "
        "JOIN types_de_poi tp ON ldtp.id_type_de_poi = tp.id "
        f"WHERE {poi_types_condition} "
        "GROUP BY dt.label_fr, dt.latitude, dt.longitude, tp.type"
    )

    # Exécution de la requête SQL
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    conn.commit()

    # Position de référence pour le filtrage des POIs
    reference_position = (received_data.result.latitude, received_data.result.longitude)

    # Filtrer les points d'intérêt dans le rayon spécifié autour de la position de référence
    list_pois = filter_pois(reference_position, rows, received_data.result.radius)

    # Utilisation de KMeans pour regrouper les POIs en clusters
    X = [(row[1], row[2]) for row in list_pois]
    kmeans = KMeans(n_clusters=10, n_init=10)
    kmeans.fit(X)
    clusters = kmeans.labels_

    # Connexion à la base de données Neo4j
    uri = "bolt://188.166.105.53:7687"
    username = "neo4j"
    password = "od1235Azerty%"

    driver = GraphDatabase.driver(uri, auth=(username, password))

    # Fonction pour créer les clusters et les POIs dans Neo4j
    def create_graph(tx):
        # Supprimer tous les nœuds et relations existants dans la base Neo4j
        tx.run("MATCH (n) DETACH DELETE n")

        # Création des clusters
        for i in range(max(clusters) + 1):
            cluster_name = f"Cluster_{i}"
            tx.run("CREATE (:Cluster {name: $name})", name=cluster_name)

        # Création des POIs et des relations avec les clusters
        for i, row in enumerate(list_pois):
            label_fr, latitude, longitude, poi_type = row
            cluster_name = f"Cluster_{clusters[i]}"
            tx.run(
                "CREATE (:POI {label_fr: $label_fr, latitude: $latitude, longitude: $longitude, poi_type: $poi_type})",
                label_fr=label_fr, latitude=latitude, longitude=longitude, poi_type=poi_type
            )
            tx.run(
                "MATCH (poi:POI {label_fr: $label_fr}), (cluster:Cluster {name: $cluster_name}) "
                "CREATE (poi)-[:BELONGS_TO]->(cluster)",
                label_fr=label_fr, cluster_name=cluster_name
            )

    # Création de la session Neo4j et exécution de la transaction
    with driver.session() as session:
        session.write_transaction(create_graph)

    # Fermeture du curseur et de la connexion à la base de données PostgreSQL
    cursor.close()
    conn.close()

    return {"status": "OK", "data": data}
