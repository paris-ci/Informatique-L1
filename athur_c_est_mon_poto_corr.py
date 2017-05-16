# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.6

"""
Correction de l'entrainement au T1 - roulette simplifiée
"""

import random

import time
import prettytable
import json
quitter = False

try:
    with open('scores.json', "r") as json_data:
        scores = json.load(json_data)
except:
    scores = {}


def main():
    jeu_termine = False
    while not jeu_termine:
        print("Bienvenue sur le jeu de la roulette simplifiée !")
        player_name = input("Entrez votre nom >").lower()
        if player_name in scores.keys():
            print("Vous avez {argent}€ a utiliser dans notre casino ! C'est parti !".format(argent=scores[player_name]))
        else:
            print("Bienvenue au casino ! Vous débutez votre aventure ici avec 500€!")
            scores[player_name] = 500

        menu = False
        while not menu:
            roulette(player_name)
            print("Vous avez {argent}€ ! ".format(argent=scores[player_name]))
            menu = not input("Voulez-vous quitter le casino ? >").lower() != "oui"

        if input("Voulez-vous quitter le jeu ? >").lower() == "oui":
            jeu_termine = True




def roulette(player):
    bien_entre = False
    while not bien_entre:
        nombre_choisi = int(input("Et si vous choissisiez un nombre sur lequel miser ? >"))
        if not 0 < nombre_choisi <= 40:
            print("Veuillez choisir un nombre entre 1 et 40 (inclus) !")
        else:
            bien_entre = True

    bien_entre = False
    while not bien_entre:
        mise = int(input("Il vous reste {argent}€ ! Veuillez entrer une mise >".format(argent=scores[player])))
        if not 0 < mise <= scores[player]:
            print("Eh, tu n'as meme pas le fric pour ca !")
        else:
            bien_entre = True
            scores[player] -= mise

    nombre_genere = random.randint(1, 40) if player != "arthur" else nombre_choisi

    print("La roulette tourne.")

    for i in range(10):
        print(".", end="")
        time.sleep(.1)

    print(" Et s'arette sur {genere}".format(genere=nombre_genere))


    if nombre_choisi == nombre_genere:
        print("OMG ! Quelle chance, vous gagnez 10x votre mise !")
        scores[player] += 10* mise
    elif nombre_choisi % 2 == nombre_genere % 2:
        print("Meme couleur, bravo ! Vous gagnez 1.5x votre mise !")
        scores[player] += 1.5 * mise
    else:
        print("Dommage, mais vous perdez cette fois-ci ! Retentez votre chance !")


try:
    main()
except KeyboardInterrupt:
    print("Bye :)")


print("Sauvegarde des scores")
with open("scores.json", "w") as file:
    json.dump(scores, file, sort_keys=True, indent=4)
            
print("\n\n\n\nMeilleurs scores du jeu :\n\n ")
x = prettytable.PrettyTable()
x._set_field_names(["nom", "argent"])
for joueur in scores.keys():
    x.add_row([joueur, scores[joueur]])
print(x.get_string(sortby="argent"))
