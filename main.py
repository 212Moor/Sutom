import csv
import random
import re

def charger_mots():
    mots = []
    with open('morphalou.csv', 'r',encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier, delimiter=';')  
        next(lecteur)  
        for ligne in lecteur:
            if ligne and len(ligne) > 1:
                mot = ligne[0].lower()
                if re.fullmatch(r'\b\w{3,6}\b', mot):  
                    mots.append(mot)
    return mots


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

def jouer(mots):
    print("Bienvenue dans Sutom!")
    mot_a_deviner = random.choice(mots)
    print("Vous avez 6 tentatives pour deviner le mot.")
    print("Le mot à deviner comporte {} lettres.".format(len(mot_a_deviner)))
    lettre_trouvee = set(mot_a_deviner[0])  
    print("Motif de départ : {}".format(afficher_motif(mot_a_deviner, mot_a_deviner[0], lettre_trouvee)))

    tentatives_restantes = 6
    while tentatives_restantes > 0:
        print("\nIl vous reste {} tentative(s).".format(tentatives_restantes))
        proposition = input("Proposez un mot: ").strip().lower()

        if len(proposition) == 1:  
            if proposition in lettre_trouvee:
                print("Vous avez déjà trouvé cette lettre.")
            elif proposition in mot_a_deviner:
                lettre_trouvee.add(proposition)
                print("Bonne devinette !")
            else:
                print("La lettre n'est pas dans le mot.")
        elif len(proposition) == len(mot_a_deviner):  
            if proposition == mot_a_deviner:
                print("Félicitations ! Vous avez deviné le mot '{}'.".format(mot_a_deviner))
                break
            else:
                print("Ce n'est pas le bon mot.")
        else:
            print("Veuillez entrer une lettre ou le mot complet de la bonne longueur.")
            continue

        correct_place, wrong_place = verifier_lettre(mot_a_deviner, proposition)
        print("Vous avez {} lettre(s) à la bonne place et {} lettre(s) à la mauvaise place.".format(correct_place, wrong_place))
        motif_actuel = afficher_motif(mot_a_deviner, proposition, lettre_trouvee)
        print("Motif actuel : {}".format(motif_actuel))

        if motif_actuel.replace(" ", "") == mot_a_deviner:
            print("Félicitations ! Vous avez deviné le mot '{}'.".format(mot_a_deviner))
            break

        tentatives_restantes -= 1

    else:
        print("Dommage ! Le mot à deviner était '{}'.".format(mot_a_deviner))

if __name__ == "__main__":
    mots = charger_mots()
    jouer(mots)
    input("Appuyez sur Entrée pour quitter...")