#!/bin/bash
# Script pour simuler le CD local avec Docker

# 1. Construire l'image Docker
docker build -t log430-a25-labo0 .

# 2. Lancer les tests
docker run --rm -it log430-a25-labo0 pytest src/tests

# 3. Optionnel : lancer l'application
# docker run --rm -it log430-a25-labo0 python src/calculator.py

# --rm → supprime le conteneur après exécution.

# -it → permet d’afficher la sortie en direct dans ton terminal.
