# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.6

"""
Nous dormons lors des cours sans défis
"""
import copy
import os
import random

from termcolor import colored


class Morpion:
    def __init__(self):
        self.morpion = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        self.state = 0
        self.tours = 0

    def __str__(self):
        s = """
Le joueur 1 sont des X, le joueur 2 les O, les non placés ne sont pas indiqués

 {a1} | {a2} | {a3}
---|---|---
 {a4} | {a5} | {a6}
---|---|---
 {a7} | {a8} | {a9}
""".format(**{
            "a1": self._affiche_char(self.morpion[0][0]),
            "a2": self._affiche_char(self.morpion[0][1]),
            "a3": self._affiche_char(self.morpion[0][2]),
            "a4": self._affiche_char(self.morpion[1][0]),
            "a5": self._affiche_char(self.morpion[1][1]),
            "a6": self._affiche_char(self.morpion[1][2]),
            "a7": self._affiche_char(self.morpion[2][0]),
            "a8": self._affiche_char(self.morpion[2][1]),
            "a9": self._affiche_char(self.morpion[2][2]),
            })

        return s

    def __len__(self):
        return self.tours

    @staticmethod
    def _affiche_char(c):
        if c == 0:
            return " "
        elif c == 1:
            return "X"
        else:
            return "O"

    @staticmethod
    def is_line_won(l):
        if l[0] != 0 and l[0] == l[1] == l[2]:
            return True, l[0]
        else:
            return False, 0

    def get_line(self, line: int):
        return self.morpion[line]

    def get_col(self, col: int):
        return [self.morpion[0][col], self.morpion[1][col], self.morpion[2][col]]

    def get_diag(self, diag: int):
        if diag == 1:
            return [self.morpion[0][0], self.morpion[1][1], self.morpion[2][2]]
        elif diag == 2:
            return [self.morpion[0][2], self.morpion[1][1], self.morpion[2][0]]
        else:
            raise ValueError

    def get_every_line(self):
        L = []
        for i in range(3):
            L.append(self.get_line(i))
            L.append(self.get_col(i))

        L.append(self.get_diag(1))
        L.append(self.get_diag(2))
        return L

    def get_available_spaces(self):
        l = []
        x = 0
        for line in self.morpion:
            y = 0
            for col in line:

                if col == 0:
                    l.append([x, y])
                y += 1
            x += 1
        return l

    def check_state(self):
        finished = True
        for l in self.get_every_line():
            if 0 in l:
                finished = False
            won, by = self.is_line_won(l)
            if won:
                self.state = by
                return won, by
        if finished:
            self.state = "draw"
            return True, "draw"

        return False, 0

    def play(self, player, line, col):
        if self.morpion[line][col] == 0:
            self.morpion[line][col] = player
            won, by = self.check_state()
            self.tours += 1
            return won, by
        else:
            raise ValueError


class IA:
    def __init__(self, player: int):
        self.player = player




class random_IA(IA):
    def move(self, m: Morpion):
        tp = random.choice(m.get_available_spaces())

        return tp[0], tp[1]


class player_IA(IA):
    def move(self, m: Morpion):
        tour_ok = False
        while not tour_ok:

            line = input_l(0, 2, "Sur quelle ligne souhaitez vous jouer ?")
            col = input_l(0, 2, "Sur quelle col souhaitez vous jouer ?")
            if [line, col] in m.get_available_spaces():
                return line, col
            else:
                print(colored("La valeur n'est pas correcte : la case est certainement déjà occupée", "red")) if SPEED else None


class premiere_classe_IA(IA):
    def move(self, m: Morpion):
        tp = m.get_available_spaces()[0]

        return tp[0], tp[1]

class preference_IA(IA):
    @staticmethod
    def get_first_common_element(x, y):
        """
        Fetches first element from x that is common for both lists
        or return None if no such an element is found.
        """
        for i in x:
            if i in y:
                return i

    def __init__(self, player: int):
        super().__init__(player)
        self.preferences = [[1, 1], [0, 0], [0, 2], [2, 2], [2, 0], [1, 0], [0, 1], [1, 2], [2, 1]]

    def move(self, m: Morpion):
        tp = self.get_first_common_element(self.preferences, m.get_available_spaces())

        return tp[0], tp[1]

class sentient_IA(IA):
    def move(self, m: Morpion):
        mc = copy.deepcopy(m)
        moves = mc.get_available_spaces()
        score = 0
        for move in moves:
            win, by =  mc.play(self.player+1, move[0], move[1])
            mc = copy.deepcopy(m)
            if win and win == self.player+1:
                return move[0], move[1]
            elif win:
                score = 2
                x, y = move[0], move[1]

            if score >= 2:
                return x, y

        if [1, 1] in moves:
            return 1, 1
        else:
            return moves[0][0], moves[0][1]






def input_l(mini, maxi, message):
    while True:
        e = False
        try:
            n = int(input(message + " [{min} | {max}] > ".format(min=mini,
                                                                 max=maxi)))
        except ValueError:
            e = True

        if not e and mini <= n <= maxi:
            return n
        print(colored("Ce nombre n'est pas correct", "red")) if SPEED else None


def main():
    g = Morpion()
    won = False
    joueur = 1

    players = [sentient_IA(0), preference_IA(1)]

    while not won:

        os.system('cls' if os.name == 'nt' else 'clear') if SPEED else None
        print(g) if SPEED else None
        print(colored("C'est au joueur {joueur} de jouer".format(**{
            "joueur": joueur
            }), "blue")) if SPEED else None

        x, y = players[joueur - 1].move(g)

        g.play(joueur, x, y)

        won, by = g.check_state()

        if won:
            if by != "draw":

                # noinspection PyUnboundLocalVariable
                print(colored("Le jeu est terminé. Le joueur {joueur} gagne !".format(**{
                    "joueur": by
                    }), "green", attrs=['blink'])) if SPEED else print(colored("Le jeu est terminé. Le joueur {joueur} gagne !".format(**{
                    "joueur": by
                }), "green"))
                print(g) if SPEED else None
                return by
            else:
                print(colored("Le jeu est terminé. Il n'y a pas de gagnant", "red"))
                print(g) if SPEED else None
                return 0

        if joueur == 1:
            joueur = 2
        else:
            joueur = 1


scores = {
    0: 0,
    1: 1,
    2: 2
}
SPEED = False
if SPEED:
    r = main()
else:
    for i in range(100000):
        r = main()

        scores[r] += 1

    print(scores)