# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""
import os
import random

import re
import csv

import sys
from tqdm import tqdm

with open("dico.txt", "r") as f:
    dico = f.read().splitlines()


def find_longest_word(L):
    return max(L, key=len)

def find_words_contains_all(letters, L):
    for word in tqdm(L):
        if all(letter in word for letter in letters):
            yield word

def find_words_contains_all_only(letters, L):
    let_set = set(letters)
    for word in L:
        if all(x in let_set for x in set(word)):
            yield word

def find_word_contains_string(string, L):
    for word in tqdm(L):
        if string in L:
            yield word

def palin(L):
    def palindrome(s):
        return s == s[::-1]

    for word in tqdm(L):
        if palindrome(word):
            yield word

def place(L, mot):
    return L.index(mot)


def scrabble_best_score(L):
    regex = re.compile('[^a-zA-Z]')
    points = dict(a=1,b=3,c=3,d=2,e=1,f=4,g=2,h=4,i=1,j=8,k=10,l=1,m=2,n=1,o=1,p=3,q=8,r=1,s=1,t=1,u=1,v=4,w=10,x=10,y=10,z=10)

    def score(mot):
        mot = regex.sub('', mot).lower()
        pt = 0
        for lettre in mot:
            pt += points[lettre]

        return pt

    return max(L, key=score)

def hazard(N):
    p = random.randint(1,N)
    cmax = N
    cmin = 1
    t = 0
    fini = False
    while not fini:
        t+= 1
        n = random.randint(cmin,cmax)
        if p < n:
            cmax = n - 1
        elif p > n:
            cmin = n + 1
        else:
            return t

def dicho(N):

    p = random.randint(1,N)
    cmax = N
    cmin = 1
    t = 0
    fini = False
    while not fini:
        t+= 1
        n = int((cmin+cmax)/2)
        if p < n:
            cmax = n - 1
        elif p > n:
            cmin = n + 1
        else:
            return t




CSV_root = os.path.dirname(os.path.realpath(sys.argv[0])) + "/results/"

tries = 100

def moyenne(func, n):
    l = []
    for i in range(tries):
        l.append(func(n))
    return int(sum(l) / len(l))


def main():

    print("EX2 - Q1\n\n")
    print(find_longest_word(dico)) #EX2 - Q1
    print("EX2 - Q2\n\n")
    print(len(list(find_words_contains_all("a", dico)))) #EX2 - Q2
    print("EX2 - Q3\n\n")
    #print(len(list(find_word_contains_string("lol", dico))))#EX2 - Q3
    print("EX2 - Q4\n\n")
    print(list(palin(dico)))#EX2 - Q4
    print("EX2 - Q5\n\n")
    print(place(dico, "mot"))#EX2 - Q5

    print("EX3 - Q1\n\n")
    print(len(list(find_words_contains_all_only("abc", dico)))) #EX3 - Q1
    print("EX3 - Q2\n\n")
    print(scrabble_best_score(dico))#EX3 - Q2

    print("EX4 - Q2\n\n")
    with open(CSV_root + "/1904EX4Q2.csv", "w") as outfile:
        outfile.write("N, random, dichotomie\n")

        for i in tqdm(range(2,100000)):
            outfile.write("{i}, {random}, {dichotomie}\n".format(**{"i" : i, "random": moyenne(hazard, i), "dichotomie" : dicho(i)}))











main()



