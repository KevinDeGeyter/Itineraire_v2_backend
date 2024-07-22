FROM python:3.9

WORKDIR /app

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
    asyncio

COPY app/AfficherCarte.py .
COPY app/Creation_Clusters.py .
COPY app/Streamlit_app.py .
COPY app/dashboard_dash.py .
COPY app/clusters_data.csv .
COPY app/clusters_map.html .
COPY app/map.html .


EXPOSE 8501 8050

# Commande par défaut pour démarrer Streamlit (à ajuster selon votre besoin)
CMD ["streamlit", "run", "Streamlit_app.py"]