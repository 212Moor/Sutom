# Cahier des Charges - Jeu du Motus en Python

:::success

## SOMMAIRE
1. Objectif
2. Fonctionnalités principales
2.1 Règles du jeu
3. Exigences techniques
4. Livrables
(DEPOT GIT DU PROJET)
:::
### 1. Objectif
L'objectif de ce projet est de développer une version du jeu du SUTOM en Python qui permettra aux utilisateurs de jouer via une interface en ligne de commande.

### 2. Fonctionnalités principales

- Génération aléatoire d'un mot à deviner.
- Affichage du mot partiellement caché avec des tirets pour les lettres non devinées.
- Réception des propositions de mots de l'utilisateur.
- Validation des propositions pour s'assurer qu'elles sont valides selon les règles du jeu du Motus.
- Affichage du nombre de lettres correctes et bien placées, ainsi que du nombre de lettres correctes mais mal placées.
- Limite de tentatives et fin de la partie si le nombre maximal de tentatives est atteint ou si le mot est deviné correctement.
- Importation d'une base de données de mots à deviner à partir d'un fichier CSV.
- Trie de la base de données pour ne sélectionner que des mots de longueur fixe et valide pour le jeu du SUTOM.


#### 2. 1 Règles du jeu




### Exigences techniques
Utilisation du language Python 
Utilisation de la bibliothèque standard Python pour la lecture de fichiers CSV.
Documentation claire et concise du code.

### Livrables

Code source Python du SUTOM.
Fichier CSV contenant la base de données des mots à deviner.
Document de conception décrivant la manière et les choix de conception du jeu.
README.md décrivant comment installer, exécuter le jeu et quelques informations 