# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""

exercice = 1
print("## Exercice " + str(exercice) + " ##")

import numpy as np

T1 = np.zeros(5)

for i in [0, 1, 4]:
    print(T1[i])

T1[3] = 5

T1[4] += 1

print(T1[:-1])
print(T1[:-2])

T2 = np.ones(5)

T3 = T1+T2
print(T3*2)


##

exercice += 1
print("## Exercice " + str(exercice) + " ##")


E2_1 =np.array([1, -1])
E2_2 = np.array([2, 3])

cd = (E2_2[1] - E2_2[0]) / (E2_1[1] - E2_1[0])

##

exercice += 1
print("## Exercice " + str(exercice) + " ##")


for i in T3:
    print(i)

for i in range(0, len(T3)):
    if T3[i] % 2 :
        T3[i] = -1
    else:
        T3[i] = 1

##

exercice += 1
print("## Exercice " + str(exercice) + " ##")


def somme(T):
    return sum(T)


print(somme(T2))

##

exercice += 1
print("## Exercice " + str(exercice) + " ##")

def minimum(T):
    return min(T)

print(minimum(T2))

##

exercice += 1
print("## Exercice " + str(exercice) + " ##")

def premier(n):
    T = np.zeros((2,n))
    for i in range(n):
        T[0,i] = i
    T[1,2:] = 1
    for i in range(2,n):
        i2 = i + i
        while i2 < n:
            T[1,i2] = 0
            i2 += i
    return T

print(premier(10))
pass

##

exercice += 1
print("## Exercice " + str(exercice) + " ##")

