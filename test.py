# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""

file = open("dico.txt","r")
T=file.read().splitlines()
cword=""
lenmax=0
for word in T:
    if len(word) > lenmax:

        cword=word
        lenmax=len(word)
        print(lenmax)

print(cword)
file.close()