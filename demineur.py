# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import shutil
from pyfiglet import figlet_format
import random

from termcolor import colored


print("\n"*shutil.get_terminal_size()[1])
class Demineur:
    def __init__(self, lines : int, cols :int, mines:int):


        self.table = []
        self.lines = lines
        self.cols = cols

        c = cols*lines
        #m = int(mines/100 * c)

        for i1 in range(lines):
            cline = []
            for i2 in range(cols):
                if random.randrange(100) <= mines:
                    cline.append('M')

                else:
                    cline.append('X')


            self.table.append(cline)



        self.mines = mines
        self.mines_restantes = mines

        self.state = None # None, "Won" or "Lost"
        self.tours = 0


    def __str__(self):

        return self.draw_board()


    def __len__(self):
        return self.tours

    def draw_board(self, mask=True):
        tstr = "  "
        for i in range(self.cols):
            tstr += " " + str(i).center(3, "-")
        tstr += "\n"
        i = 0
        for ligne in self.table:
            tstr += str(i).center(2)
            i += 1
            for element in ligne:

                elems = {
                    '0' : colored('0', 'green'),
                    '1' : colored('1', 'yellow'),
                    '2' : colored('2', 'cyan'),
                    '3' : colored('3', 'magenta'),
                    '4' : colored('4', 'red'),
                    '5' : colored('5', 'red'),
                    '6' : colored('6', 'red'),
                    '7' : colored('7', 'red'),
                    '8' : colored('8', 'red'),
                    'K' : colored('K', 'red', 'on_yellow'),
                    'Fm' : colored('F', 'grey', 'on_red'),
                    'Fx' : colored('F', 'grey', 'on_red'),
                }
                if element in elems.keys():
                    element = elems[element]
                else:
                    if mask:
                        element = '-'
                tstr += "| " + element + " "
            tstr += "|\n"
        tstr += "  "
        tstr += " ---"* self.cols
        return tstr

    def current(self):
        return self.draw_board(mask=False)

    def get_near(self, line, col):
        """Retourne la liste des cases voisines de (line,col)."""
        r = [(line, col - 1), (line + 1, col - 1), (line + 1, col), (line + 1, col + 1), (line, col + 1), (line - 1, col + 1), (line - 1, col), (line - 1, col - 1)]
        asup = []
        for i in r:
            if i[0]<0 or i[1]<0 or i[1]>(self.cols-1) or i[0]>(self.lines-1):
                asup.append(i)
        for i in asup:
            r.remove(i)
        return r

    def get_NbMines_near(self, line, col):
        """Retourne le nombre de mines voisines de (l,c)."""
        r = 0
        for i in self.get_near(line, col):
            if self.table[i[0]][i[1]] == 'M' or self.table[i[0]][i[1]] == 'Fm':
                r += 1

        return r

    def _clean_space(self, line, col):
        m = self.get_NbMines_near(line, col)
        self.table[line][col] = str(m)
        if m == 0:

            for line1, col1 in self.get_near(line, col):
                if self.table[line1][col1] == "X" or self.table[line1][col1] == "Fx":
                    m = self.get_NbMines_near(line1, col1)
                    if m == 0:
                        self.table[line1][col1] = '0'
                        self._clean_space(line1, col1)
                    else:
                        self.table[line1][col1] = str(m)


    def devoiler(self, line, col, flag):
        try:
            if self.table[line][col] in ['X', 'M', 'Fm', 'Fx']:
                self.tours += 1
                if self.table[line][col] == 'Fx' and flag:
                    self.table[line][col] = 'X'
                    return True
                elif self.table[line][col] == 'Fm' and flag:
                    self.table[line][col] = 'M'
                    return True
                elif flag:
                    self.table[line][col] = 'F' + self.table[line][col].lower()
                    return True

                if self.table[line][col] == 'M' or self.table[line][col] == 'Fm':
                    self.mines_restantes -= 1
                    self.table[line][col] = 'K'
                    self.state = "Lost"
                else:
                    self._clean_space(line, col)
                return True
            else:
                return False
        except IndexError:
            return False

    def check_finished(self):
        for i1 in range(self.lines):
            for i2 in range(self.cols):
                if self.table[i1][i2] == 'X':
                    return False

        self.state = "Won"
        return True



lines, cols, mines =  int(input("Combien de lignes ? > ")), int(input("Combien de colonnes ? > ")), int(input("Combien de mines (en pct) ? > "))


r = True
while r:
    d = Demineur(lines, cols, mines)
    print("\n"*100)

    print(figlet_format('Bienvenue sur le', font='starwars', width=shutil.get_terminal_size()[0]))
    print(figlet_format('DEMINEUR', font='starwars', width=shutil.get_terminal_size()[0]))

    while d.state is None:

        if d.check_finished():
            print(colored(figlet_format('VOUS AVEZ GAGNE ! BRAVO !', font='starwars', width=shutil.get_terminal_size()[0]), 'green'))
        else:
            try:
                print(str(d))
                l = int(input("Sur quelle ligne voulez-vous jouer ? > "))
                c = int(input("Sur quelle colonne voulez-vous jouer ? > "))
                f = "f" in input("Placer un drapeau ([f]lag) ou [d]écouvrir une case ? > ")
                print("\n"*shutil.get_terminal_size()[1])
                if not d.devoiler(l, c, f):
                    print(colored('Veuillez entrer des coordonnées correctes...', 'red'))
            except ValueError:
                print(colored('Veuillez entrer des coordonnées correctes...', 'red'))



    print(figlet_format('Fin de la partie !', font='starwars', width=shutil.get_terminal_size()[0]))
    print(d.current())
    if input("Voulez vous rejouer avec les memes réglages ? [y/n] > ").lower() == "n":
        r = False







