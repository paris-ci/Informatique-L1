# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5
"""
Informatique -- des
"""
import logging


# from logging.handlers import RotatingFileHandler
import random


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
    logger.addHandler(steam_handler)
    return logger

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Des(metaclass=Singleton):
    def __init__(self):
        self.face = None

    def lance(self):
        self.face = random.randint(1,6)

def main():
    des1 = Des()
    des1.lance()
    print(des1.face)
    des2 = Des()
    if des1 == des2:
        print("ok")
        if des1.face == des2.face:
            print("ok2")


logger = createLogger()

logger.info('Initialisation terminée')

__author__ = "Arthur — paris-ci"
__licence__ = "WTFPL — 2016"

if __name__ == '__main__':
    main()

