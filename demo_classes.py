# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import random


class Jeu:
    def __init__(self, titre: str):
        self.utilise = False
        self.complet = True
        self.titre = titre

    def jouer(self, joueur1, joueur2):
        self.utilise = True
        print("Vous jouez au jeu " + self.titre + "!")

    def ranger(self):
        self.utilise = False
        print("Vous rangez le jeu " + self.titre + "!")


class JeuDeCartes(Jeu):
    def __init__(self, titre: str):
        super().__init__(titre)
        self.trie = True
        self.cartes = [1, 2, 3, 4, 5, 6]
        self.nbcartes = len(self.cartes)

    def trier(self):
        print("Vous triez le jeu de cartes " + self.titre + "!")
        self._verifier_jeu_complet()
        self.trie = True

    def melanger(self):
        print("Vous mélangez le jeu de cartes " + self.titre + "!")
        self.utilise = False
        self.trie = False
        if random.choice([True, False]):
            self.cartes.pop()

    def _verifier_jeu_complet(self):
        if len(self.cartes) == self.nbcartes:
            print("Le jeu de cartes " + self.titre + " est complet!")
            self.complet = True
        else:
            print("Le jeu de cartes " + self.titre + " est incomplet!")
            self.complet = False

    def racheter(self):
        self.__init__(self.titre)


class Monopoly(Jeu):
    def __init__(self):
        super().__init__("Monopoly de Paris")
        self.plateau_pret = False
        self.pions_jeu = ["dés à coudre", "chapeau", "voiture", "bateau", "cheval", "poubelle"]
        self.pions = self.pions_jeu[:]

    def ouvrir_plateau(self):
        self.plateau_pret = True

    def choisir_pion(self, pion):
        if pion in self.pions:
            self.pions.remove(pion)
        else:
            raise ValueError("Pion non disponible !")


tweet = \
    {
        "texte"    : "La Caroline du Nord recule dans la «bataille des toilettes» #AFP",
        "hashtags" : ["AFP"],
        "mots clés": ["Caroline du Nord", "bataille des toilettes"],
        "envoyeur" :
            {
                "nom"             : "Sébastien Blanc",
                "handle"          : "@sebastienblanc",
                "verified"        : True,
                "derniers tweets" : [],
                "inscrit"         : "mai 2009",
                "nombre de tweets": 1756
            },
        "lien"     : "https://t.co/qEXxN9cqS2",
        "domaine"  : "lapresse.ca",
        "retweet"  : 1,
        "favoris"  : 1,
        "permalink": "https://twitter.com/sebastienblanc/status/847535182550884354",
        "son_jeu"  : Monopoly(),
        2          : "prout"

    }
