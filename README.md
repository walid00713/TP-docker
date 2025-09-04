# TP Docker

##  Objectif
Se familiariser avec Docker : installation, manipulation de conteneurs, création d’images, déploiement d’applications simples et utilisation de **docker-compose**.

---

##  Tâches réalisées

### 1. Installation de Docker
- Installation de Docker Desktop / Docker Engine.
- Vérification de l’installation avec :
  ```bash
  docker --version
  ```

### 2. Manipulation de base des conteneurs
- Vérification de la version de Docker.
- Liste des images locales avec :
  ```bash
  docker images
  ```
- Téléchargement de l’image `hello-world`.
- Exécution d’un conteneur `hello-world`.
- Liste des conteneurs actifs et stoppés.
- Suppression d’un conteneur et d’une image.

### 3. Création d’un serveur web avec Docker
- Téléchargement de l’image **nginx**.
- Lancement d’un conteneur Nginx sur le port 8080.
- Vérification de l’accès à la page web par navigateur.
- Arrêt et suppression du conteneur.

### 4. Déploiement d’une application Python Flask
- Création d’une application Flask minimaliste (`app.py`).
- Écriture d’un `Dockerfile` pour construire l’image.
- Construction et lancement de l’image de l’application.
- Vérification du bon fonctionnement via navigateur.

### 5. Utilisation de Docker Compose
- Modification de l’application Flask pour ajouter une connexion à MongoDB.
- Création d’un fichier `docker-compose.yml` pour lancer **Flask + MongoDB**.
- Lancement du `docker-compose`.
- Vérification de la connexion à la base MongoDB.

---

## Cheatsheet utilisée
- `docker pull <image>` : télécharger une image
- `docker run <image>` : exécuter un conteneur
- `docker ps / docker ps -a` : lister les conteneurs
- `docker stop <id>` : arrêter un conteneur
- `docker rm <id>` : supprimer un conteneur
- `docker rmi <id>` : supprimer une image
- `docker build -t <nom_image> .` : construire une image
- `docker exec -it <id> bash` : entrer dans un conteneur
- `docker-compose up -d` : lancer une stack docker-compose
- `docker-compose down` : arrêter les services

---

## 🏁 Conclusion
À travers ce TP, j’ai pu :
- Apprendre les commandes Docker de base.
- Créer et déployer un serveur web avec Nginx.
- Développer et dockeriser une application Flask.
- Déployer une application multi-conteneurs avec **Docker Compose** et MongoDB.
