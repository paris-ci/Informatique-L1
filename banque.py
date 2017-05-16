# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
Informatique -- banque
"""
import logging


# from logging.handlers import RotatingFileHandler

def createLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    # file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)
    steam_handler = logging.StreamHandler()
    steam_handler.setLevel(logging.DEBUG)
    steam_handler.setFormatter(formatter)
    logger.addHandler(steam_handler)
    return logger

class CompteBancaire:
    def __init__(self, nomTitulaire, soldeInitial = 1000):
        self.titutulaire = nomTitulaire
        self.solde = soldeInitial

    def _ajouterArgent(self, somme):
        self.solde += somme

    def _retirerArgent(self, somme):
        self.solde -= somme

    def virementArgent(self, compteReceveur, somme):
        if self.solde >= somme:
            self._retirerArgent(somme)
            compteReceveur.solde += somme
            return True
        else:
            print("Opération impossible, vous n'avez pas assez d'argent")
            return False

    def retrait(self, somme):
        if self.solde >= somme:
            self._retirerArgent(somme)
            print("Vous retirez " + str(somme) + "€")
        else:
            print("Opération impossible, vous etes à découvert !")

    def depot(self, somme):
        self._ajouterArgent(somme)
        print("Vous ajoutez " + str(somme) +  "€ à votre compte.")

    def printSolde(self):
        print("Le compte de " + self.titutulaire + " dispose de " + str(self.solde) + "€.")



def main():
    c1 = CompteBancaire("Arthur JOVART")
    c2 = CompteBancaire("Villebon Charpak")

    c2.virementArgent(c1, 200) # Virement de Villebon vers Arthur
    print("Le compte de " + c1.titutulaire + " ")


logger = createLogger()

logger.info('Initialisation terminée')

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

if __name__ == '__main__':
    main()

