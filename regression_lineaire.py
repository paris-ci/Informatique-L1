# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model


regr = linear_model.LinearRegression()


x = [ 1/-26, 1/-(40.6-23.5), 1/-(37.4-23.5), 1/-(45.2-23.5), 1/-(38.3-23.5), 1/-(37-23.5), 1/-(39-23.5), 1/-(36.5-23.5), 1/-(40-23.5), 1/-(36.5-23.5)] # OA
y = [ 1/19.4, 1/(73.5 - 40.6), 1/(109.5-37.4), 1/(68.8-45.2), 1/(92.6-38.3), 1/(149-37), 1/(88.3-39), 1/(172.4-23.5), 1/(79.8-40), 1/(185.3-36.5)] # OA'
grandissement = [ -0.4/0.5, -1/0.5, -2.8/0.5, -1, -4.7/0.5, -5.5/0.5, -1.6/0.5 , -5.8/0.5, -1.4/0.5, -6.5/0.5]
assert len(x) == len(y) == len(grandissement)
print("Nombre de valeurs : " + str(len(x)))

print("x = " + str(x))
print("y = " + str(y))
print("g = " + str([g for g in grandissement]))

print("x2 = " + str([1/y1 for y1 in y]))
