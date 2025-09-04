from flask import Flask
from pymongo import MongoClient
import os
import time

app = Flask(__name__)

mongo_host = os.environ.get("MONGO_HOST", "mongodb")
mongo_port = int(os.environ.get("MONGO_PORT", 27017))

# Retry connexion MongoDB
for i in range(10):
    try:
        client = MongoClient(host=mongo_host, port=mongo_port, serverSelectionTimeoutMS=2000)
        client.server_info()
        print("✅ Connexion à MongoDB réussie.")
        break
    except Exception as e:
        print(f"⏳ Tentative {i+1}/10 : MongoDB pas encore prêt ({e})")
        time.sleep(2)
else:
    print("❌ Impossible de se connecter à MongoDB après plusieurs tentatives.")
    exit(1)

db = client["ma_base"]
collection = db["test"]

@app.route('/')
def home():
    collection.insert_one({"message": "Connexion réussie !"})
    count = collection.count_documents({})
    return f"Connexion MongoDB OK - {count} documents dans la collection."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
