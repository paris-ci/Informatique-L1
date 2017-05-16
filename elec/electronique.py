# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
Informatique -- electronique
"""
import logging

# from logging.handlers import RotatingFileHandler
import time


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


def main():
    time.sleep(.1)
    fonction = input("Entrez la fonction a tester (no, yes, and, or , xor)  >> ").lower()
    time.sleep(.1)

    A = bool(input("Entrez la valeur de A : 0 / 1  >> "))
    if fonction == "no":
        logger.info("Valeur de sortie pour A = \"{A}\" : \"{val}\" ".format(**{"val": not A, "A": A}))
        return True
    elif fonction == "yes":
        logger.info("Valeur de sortie pour A = \"{A}\" : \"{val}\" ".format(**{"val": A, "A": A}))
        return True

    time.sleep(.1)
    B = bool(input("Entrez la valeur de B : 0 / 1  >> "))

    if fonction == "and":
        logger.info("Valeur de sortie pour A = \"{A}\" et B = \"{B}\" : \"{val}\" ".format(**{"val": A and B, "A": A, "B": B}))
        return True
    elif fonction == "or":
        logger.info("Valeur de sortie pour A = \"{A}\" et B = \"{B}\" : \"{val}\" ".format(**{"val": A or B, "A": A, "B": B}))
        return True
    elif fonction == "xor":
        logger.info("Valeur de sortie pour A = \"{A}\" et B = \"{B}\" : \"{val}\" ".format(**{"val": A and not B or B and not A, "A": A, "B": B}))
        return True
    else:
        logger.info("Lapin compris. Essaye avec no, yes, and, or ou xor")
        return False


logger = createLogger()

logger.info('Initialisation terminée')

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

if __name__ == '__main__':
    while main():
        pass
