import csv
import random
import re


""" Cette fonction charge les mots à partir d'un fichier CSV nommé morphalou.csv. Elle utilise le module csv pour lire le fichier ligne par ligne et récupérer les mots. Les mots sont ensuite filtrés pour s'assurer qu'ils ont une longueur comprise entre 3 et 6 caractères et sont ajoutés à une liste. Enfin, la liste de mots est renvoyée. """
def charger_mots():
    mots = []
    with open('morphalou.csv', 'r') as fichier:
        lecteur = csv.reader(fichier, delimiter=';')  
        next(lecteur)  
        for ligne in lecteur:
            if ligne and len(ligne) > 1:
                mot = ligne[0].lower()
                if re.fullmatch(r'\b\w{3,6}\b', mot):  
                    mots.append(mot)
    return mots

""" Cette fonction prend une liste de mots, une longueur de mot et une première lettre comme arguments. Elle filtre les mots de la liste en ne gardant que ceux qui ont la longueur spécifiée et commencent par la lettre spécifiée. Elle retourne la liste des mots filtrés. """
def filtrer_mots(mots, longueur_mot, premiere_lettre):
    return [mot for mot in mots if len(mot) == longueur_mot and mot.startswith(premiere_lettre)]


""" Cette fonction prend un mot à deviner et une proposition de mot comme arguments. Elle compare chaque lettre de la proposition avec celle du mot à deviner pour déterminer le nombre de lettres correctement placées et le nombre de lettres correctes mais mal placées. Elle retourne ces deux valeurs. """
def verifier_lettre(mot, proposition):
    correct_place = 0
    wrong_place = 0
    lettres_correctes = set()
    lettres_proposees = set()
    for i in range(len(mot)):
        if proposition[i] == mot[i]:
            correct_place += 1
            lettres_correctes.add(proposition[i])
        else:
            lettres_proposees.add(proposition[i])
    for lettre in lettres_proposees:
        if lettre in mot and lettre not in lettres_correctes:
            wrong_place += 1
    return correct_place, wrong_place

""" Cette fonction prend un mot à deviner, une proposition de mot et un ensemble de lettres trouvées comme arguments. Elle génère un motif qui représente les lettres correctement devinées, les lettres correctes mais mal placées et les lettres non devinées. Elle retourne ce motif. """
def afficher_motif(mot, proposition, lettre_trouvee):
    motif = ""
    for i in range(len(mot)):
        if i < len(proposition):  
            if proposition[i] == mot[i]:
                motif += proposition[i] + ""  
            elif proposition[i] in mot:
                motif += "_"  
            else:
                motif += "_"  
        else:
            motif += "_"  
    return motif.strip()

""" Cette fonction représente le jeu principal. Elle commence par choisir aléatoirement une longueur de mot et une première lettre, puis charge les mots correspondants à partir du fichier CSV. Ensuite, elle filtre les mots en fonction de la longueur et de la première lettre choisies. Si aucun mot ne correspond aux critères, le jeu se termine. Sinon, un mot à deviner est choisi aléatoirement parmi les mots filtrés. L'IA propose ensuite des mots tant qu'elle n'a pas trouvé le mot à deviner ou qu'elle a épuisé toutes ses tentatives. Pour chaque proposition, elle vérifie les lettres correctement placées et mal placées, affiche le motif actuel du mot à deviner, et vérifie si le mot a été entièrement deviné. Enfin, elle affiche un message de félicitations ou de défaite en fonction du résultat. """
def jouer_ia():
    print("Bienvenue dans Sutom!")
    longueur_mot = random.randint(3, 6) 
    premiere_lettre = chr(random.randint(97, 122))  
    mots = charger_mots()
    mots_filtres = filtrer_mots(mots, longueur_mot, premiere_lettre)
    if not mots_filtres:
        print("Aucun mot correspondant aux critères n'a été trouvé.")
        return

    mot_a_deviner = random.choice(mots_filtres)
    print("Le mot à deviner comporte " + str(len(mot_a_deviner)) + " lettres.")
    lettre_trouvee = set(mot_a_deviner[0])  
    print("Motif de départ : " + afficher_motif(mot_a_deviner, mot_a_deviner[0], lettre_trouvee))

    tentatives_restantes = 6
    while tentatives_restantes > 0:
        proposition = random.choice(mots_filtres)
        print("L'IA propose le mot :" + proposition)
        correct_place, wrong_place = verifier_lettre(mot_a_deviner, proposition)
        print("Vous avez " + str(correct_place) + " lettre(s) à la bonne place et " + str(wrong_place) + " lettre(s) à la mauvaise place.")
        motif_actuel = afficher_motif(mot_a_deviner, proposition, lettre_trouvee)
        print("Motif actuel :" + motif_actuel)

        if motif_actuel.replace(" ", "") == mot_a_deviner:
            print("Félicitations ! L'IA a deviné le mot : " + mot_a_deviner + ".")
            break

        tentatives_restantes -= 1

    else:
        print("Dommage ! Le mot à deviner était " + mot_a_deviner + ".")

if __name__ == "__main__":
    jouer_ia()
