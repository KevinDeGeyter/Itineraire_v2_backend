FROM python:3.9

WORKDIR Itineraire

RUN pip install --no-cache-dir \
    neo4j \
    scikit-learn \
    psycopg2-binary \
    geopy \
    streamlit \
    folium \
    openrouteservice \
    streamlit_folium \
    dash \
    plotly \
    asyncio \
    fastapi \
    bcrypt \
    beanie \
    email-validator \
    httpx \
    Jinja2 \
    motor \
    passlib \
    pytest \
    python-multipart \
    python-dotenv \
    python-jose \
    sqlmodel \
    uvicorn \

COPY app/AfficherCarte.py .
COPY app/Creation_Clusters.py .
COPY app/Streamlit_app.py .
COPY app/clusters_data.csv .
COPY app/clusters_map.html .
COPY app/map.html .

RUN mkdir dash
COPY dash/dashboard_dash.py dash

RUN mkdir -p backend/routers
COPY backend/main.py backend
COPY backend/routers/__init__.py backend/routers
COPY backend/routers/tripadvisor.py backend/routers

# EXPOSE 8050 8051
# Commande par défaut pour démarrer Streamlit (à ajuster selon votre besoin)
# CMD ["streamlit", "run", "Streamlit_app.py"]
# ENTRYPOINT ["streamlit", "run", "Streamlit_app.py"]