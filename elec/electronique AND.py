# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
Informatique -- electronique AND
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


def main():
    logger.info("{A} | {B} | {Rin} == {S} | {Rout}".format(**{
        "A"   : "A",
        "B"   : "B",
        "Rin" : "Rin",
        "Rout": "Rout",
        "S"   : "S"
    }))
    for A in range(0, 2):
        for B in range(0, 2):
            for Rin in range(0, 2):
                A = bool(A)
                B = bool(B)
                Rin = bool(Rin)
                logger.info("{A} | {B} | {Rin}  ==  {S} | {Rout}".format(**{
                    "A"   : int(A),
                    "B"   : int(B),
                    "Rin" : int(Rin),
                    "Rout": int((A and B) or (Rin and (A != B))),
                    "S"   : int(Rin != (A != B))
                }))


logger = createLogger()

logger.info('Initialisation terminée')

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

if __name__ == '__main__':
    main()
