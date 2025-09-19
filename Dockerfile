# image de base Python légère
FROM python:3.11-slim

# variables d'environnement (éviter la mise en cache des fichiers pyc)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copier requirements et installer pour tirer parti du cache Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
