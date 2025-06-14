# Conception du jeu SUTOM
## SOMMAIRE 
1. Introduction
2. Structure de données
3. Fonctions principales
4. Organisation des fichiers
5. Organisation des Groupes
6. Commandes / Fichiers tests
7. Execution du programme
8. Organisation

#### 1. Introduction

Le jeu du SUTOM est un jeu de réflexion dans lequel le joueur doit deviner un mot à partir d'indices fournis par le jeu. Le joueur a un nombre limité de tentatives pour deviner le mot correctement. Ce document décrit la conception du jeu du Motus en Python.

#### 2. Structure de données

Le jeu utilise une liste de mots chargés à partir d'un fichier CSV. Ces mots servent de base de données à partir de laquelle le jeu choisit aléatoirement le mot à deviner.

#### 3. Fonctions principales

a. charger_mots(fichier_csv)
Cette fonction charge les mots à partir du fichier CSV fourni en paramètre. Elle filtre les mots en ne retenant que ceux de longueur comprise entre 5 et 7 lettres.

b. verifier_lettre(mot, proposition)
Cette fonction vérifie les lettres proposées par le joueur par rapport au mot à deviner. Elle renvoie le nombre de lettres correctement placées et le nombre de lettres correctes mais mal placées.

c. jouer(mots)
Cette fonction implémente le déroulement du jeu. Elle choisit aléatoirement un mot parmi la liste de mots chargée, puis demande au joueur de deviner le mot en proposant des mots. Elle gère également le décompte des tentatives et fournit des indices pour aider le joueur.

##### Tableau de dépendances du code:

https://urlz.fr/qfn8
#### 4. Organisation des fichiers


main.py: Contient les fonctions principales du jeu.
morphalou.csv: Fichier CSV contenant la base de données de mots à deviner.
README.md: Fichier Markdown décrivant comment installer, exécuter et jouer au jeu.
docs/ conception.md and cdc.md contient le document de conception et le cahier des charges

#### 5. Organisation des Groupes

-Projet complété par le groupe ->

Composition du Groupe : 
- CASTANHO Kevin
- OUKOUIS Soufiane

Composition de notre groupe(2) :
- AMMOR Zakariyaa
- TAHRI Shahine 


#### 6. Commandes / Fichiers Tests


Exécution du programme :
Pour jouer au jeu, téléchargez les fichiers sutom.py et morphalou.csv dans un même dossier, puis exécutez le fichier sutom.py. Suivez les instructions pour deviner le mot proposé.

#### 7. Execution du programme


#### 8. Organisation

Développement de la fonction charger_mots et tests de validation des données du fichier CSV.
Puis implémentation de la logique de jeu principale dans jouer et gestion des interactions utilisateur.
- Revue de code : Les membres du groupe effectueront des revisions du code pour s'assurer de la qualité et du fonctionnement du code.
- Gestion du projet grace à une communication régulière.

- Difficultés anticipées
Gestion des erreurs de saisie utilisateur : Assurer que le jeu gère efficacement les entrées incorrectes sans planter.
Compatibilité : Faire en sorte que le jeu fonctionne de manière cohérente sur différentes plateformes (Windows, macOS, Linux).


-Répartition des tâches, les difficultés rencontrées (techniques / prise en main du code d'un autre groupe, etc.)
Nous leur avons donné les permissions sur notre dépôt git. Nous avons effectué la création d'une nouvelle branche et push des nouveautés dans cette même branche.
-Fonctionnement:
Discuter, répartir les tâches de manière cohérente
Organiser chaque fichier dans un seul dossier/endroit. Par exemple: Replit
Faire des checkpoints régulièrement (correction bug, validation, avancement...)