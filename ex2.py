# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
exercice = 0
#from stackoverflow import prime_numbers

#import random
# for nombre in prime_numbers.erat3():
#     print(nombre)
#     if random.randint(0,100) == 1:
#         break

from matplotlib import pyplot as plt
import numpy as np

def Verhulst(t0, tn, S0, n):
    liste_val = [S0]
    intervalle = (tn - t0) / n

    for i in range(n):
        liste_val.append(liste_val[i] + 0.2 * intervalle * liste_val[i] * ( 1 - liste_val[i]/10 ))
    return liste_val

# Q3
n = 1000
t0 = 0
tn = 100
S0 = 1
x = np.arange(t0,tn-t0+((tn-t0)/n),(tn-t0)/n)
y = Verhulst(t0, tn, S0, n)

plt.plot(x,y)

#Q4
n = 100
t0 = 0
tn = 1
S0 = 11
x = np.arange(t0,tn-t0+((tn-t0)/n),(tn-t0)/n)
y = Verhulst(t0, tn, S0, n)
plt.plot(x,y)


plt.show()