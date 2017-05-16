"""
DM interdisciplinaire 1 -Parti Info-
Pascal BEROULE
"""

# 1
from math import sqrt
from math import exp
import numpy as np
from matplotlib import pyplot as plt

#2

V = [0.83, 0.83, 0.84, 0.82, 0.83, 0.82, 0.85, 0.81, 0.83, 0.84]

#3
# t -> total des valeus du tableau
# m -> moyenne

t = 0

for i in V:
    t+=i
m = t/10
print("moyenne =",m)

#4
# E -> ecart type
# i -> incertitude

E = 0

for i in V:
    E+=(i-m)**2
E = sqrt(E/10)
i = E/(sqrt(10))

print("ecart type =",E)
print("incertitude =",i)

###5
### e -> exp
### d -> dérivée de exp
##
##e = []
##d = []
##diff = []
##p = 0.000000000000001 #valeur la plus petite possible
##
##def drv(x):
##    drv = (exp(i)-(exp(i-p)))/(i-p)
##    return drv
##
##for i in range (11):
##    e.append(exp(i))
##    d.append(drv(i))
##    diff.append(e[i-1]-d[i-1])
##
##print(diff) # devrait valoir 0

"""
on ne peut pas avoir une valeur de p suffisemment petite pour avoir exp(x) = exp'(x)
mais la définition d'exonentielle est que la valeur d'exp(x) est égale à dérivée. l'exponentielle est donc solution de l'équation y(x) = y'(x)
"""

#6

def num (i):
    i = 10/i
    S = np.arange(0, 10+i, i)
    return S

T1 = num(10)
T2 = num(100)

print(T1)
print(T2)

#7

def euler(y0, N):
    T = num(N)
    i = 10/N
    n = y0
    l = []
    for e in T:
        l.append(n)
        n= (i+1)*n
    return l

#8

Y1 = euler(1,10)
Y2 = euler(1,100)

#9

Y3 = []

for i in T2:
    Y3.append(exp(i))

#10

plt.plot(T1, Y1)
plt.plot(T2, Y2)
plt.plot(T2, Y3)

plt.show()