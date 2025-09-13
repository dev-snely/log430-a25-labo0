# Rapport de laboratoire – Déploiement continu avec GitHub Actions et Docker

## Question 1 : Si l’un des tests échoue à cause d’un bug, comment pytest signale-t-il l’erreur et aide-t-il à la localiser ?

`pytest` signale les erreurs en indiquant :

- Le fichier où l’erreur se produit
- La ligne exacte qui a causé l’échec
- La nature de l’exception

Exemple de test volontairement erroné dans `tests/test_calculator.py` :

```python
def test_addition():
    addition()  # Erreur volontaire : addition() n’existe pas
```

Sortie terminal :
```bash
========================================== FAILURES ==========================================
_______________________________________ test_addition ________________________________________

    def test_addition():
>       addition()
        ^^^^^^^^
E       NameError: name 'addition' is not defined

tests/test_calculator.py:14: NameError
================================== short test summary info ===================================
FAILED tests/test_calculator.py::test_addition - NameError: name 'addition' is not defined
================================ 1 failed, 1 passed in 0.03s =================================
```

## Question 2 : Que font les étapes setup et checkout dans GitHub Actions ?

**Setup** : prépare l’environnement pour le workflow. Une machine virtuelle Ubuntu est lancée, Python est installé automatiquement (ici 3.12) et ajouté au PATH pour être utilisé directement.

Sortie terminal exemple :
```bash
Run actions/setup-python@v4
  with:
    python-version: 3.12
Installed versions
  Successfully set up CPython (3.12.11)
  
```

**Checkout** : récupère le code source du dépôt dans le runner, configure Git (safe directory, authentification via GITHUB_TOKEN) et extrait la révision correspondant au commit déclencheur du workflow.

Sortie terminal exemple :

```bash
Run actions/checkout@v3
Syncing repository: dev-snely/log430-a25-labo0
Fetching the repository
Checking out the ref
/usr/bin/git log -1 --format='%H'
'1cdb859cd6021d89b5ff908f39e73191a2ecdc95'

```

## Question 3 : Quel approche et quelles commandes avez-vous exécutées pour automatiser le déploiement continu de l'application dans la machine virtuelle ?

**Approche** : 

- Installer un runner GitHub auto-hébergé sur la VM.  
- Créer un script deploy.sh qui :  
  - Va dans le répertoire du projet  
  - Fait un git pull pour récupérer les dernières modifications  
  - Construit l’image Docker  
  - Lance les tests avec pytest  
  - Optionnellement, lance l’application  

**Script** `deploy.sh` :
```bash
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
# docker run --rm -it log430-a25-labo0 python src/main/calculator.py

# --rm → supprime le conteneur après exécution.

# -it → permet d’afficher la sortie en direct dans ton terminal.
echo "Déploiement terminé !"
```

J'ai un service qui lance le runner et part le script de déploiement à l'ouverture de la VM, donc un: 
`docker run --rm -it log430-a25-labo0 python src/main/calculator.py` permet de partir l'application directement.

## Question 4 : Quel type d'informations pouvez-vous obtenir via la commande top ?
top fournit un aperçu en temps réel de l’utilisation des ressources :

PID : identifiant du processus

USER : utilisateur exécutant le processus

PR, NI : priorité et nice value

VIRT, RES, SHR : mémoire virtuelle, mémoire résidente et partagée

S : état du processus (S=sleeping, R=running, etc.)

%CPU : pourcentage d’utilisation CPU

%MEM : pourcentage d’utilisation RAM

TIME+ : temps CPU total consommé

COMMAND : commande lancée

``` bash
  PID USER      PR  NI    VIRT    RES   SHR S  %CPU %MEM     TIME+ COMMAND
  848 root      20   0 1802284  47912 34432 S   0.3  1.3 12:27.52 containerd
```
En résumé : containerd tourne en arrière-plan, utilise très peu de CPU (~0,3%), consomme 1,3 % de la mémoire totale, et est actuellement en veille (S).