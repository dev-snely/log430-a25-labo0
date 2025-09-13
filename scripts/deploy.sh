#!/bin/bash
# Script pour le déploiement continu avec Docker sur la VM

set -e  # Stoppe le script si une commande échoue

# Se placer dans le projet local
cd ~/log430-a25-labo0 || exit


# Aller dans le répertoire du projet
PROJECT_DIR=~/log430-a25-labo0
cd "$PROJECT_DIR" || { echo "Impossible d'accéder à $PROJECT_DIR"; exit 1; }
echo "Mise à jour du code source..."
git pull origin main  # Récupère les derniers changements

# Construire l'image Docker
echo "Construction de l'image Docker..."
docker build -t log430-a25-labo0 .

# Lancer les tests
echo "Exécution des tests..."
docker run --rm log430-a25-labo0 pytest src/tests

# 3. Optionnel : lancer l'application
# docker run --rm -it log430-a25-labo0 python src/calculator.py

# --rm → supprime le conteneur après exécution.

# -it → permet d’afficher la sortie en direct dans ton terminal.
echo "Déploiement terminé !"
