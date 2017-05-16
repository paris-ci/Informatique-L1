# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
Informatique -- electdm
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

def S2(O1,O2,O3):
    return not((not O3) and not((not O2) and O1))

def main():
    for O1 in range(2):
        for O2 in range(2):
            for O3 in range(2):
                logger.info("{O1} | {O2} | {O3} || {S1} | {S2}".format(**{"O1": O1, "O2": O2, "O3": O3, "S1": int(O2), "S2": int(S2(O1,O2,O3))}))


logger = createLogger()

logger.info('Initialisation terminée')

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

if __name__ == '__main__':
    main()

