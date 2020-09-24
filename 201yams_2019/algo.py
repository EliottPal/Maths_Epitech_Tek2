##
## EPITECH PROJECT, 2020
## 201yams_2019
## File description:
## algo
##

import math

def yams(dice, A):
    res = 0
    for die in dice:
        if res == 0 and die != A:
            res = 1.0 / 6.0
        elif die != A:
            res *= 1.0 / 6.0
    print("Chances to get a %d yams: %.2f%%" % (A, res * 100))

def straight(dice, A):
    which = 6 if (A == 6) else 1
    here = [0, 0, 0, 0, 0]
    res = 0
    startof = 0
    for die in dice:
        if int(die) == 2 and here[0] == 0:
            here[0] = 1
        elif int(die) == 3 and here[1] == 0:
            here[1] = 1
        elif int(die) == 4 and here[2] == 0:
            here[2] = 1
        elif int(die) == 5 and here[3] == 0:
            here[3] = 1
        elif int(die) == 6 and which == 6 and here[4] == 0:
            here[4] += 1
        elif int(die) == 1 and which == 1 and here[4] == 0:
            here[4] += 1
    res = here[0] + here[1] + here[2] + here[3] + here[4]
    res = math.factorial(5 - res) / math.pow(6, (5 - res))
    print("Chances to get a %d straight: %.2f%%" % (A, (res * 100)))

def full(dice, third, twice):
    amount2 = dice.count(twice)
    amount3 = dice.count(third)
    if (amount3 > 3):
        amount3 = 3
    if (amount2 > 2):
        amount2 = 2
    if amount3 == 3 and amount2 == 2:
            res = 100
    pair = math.factorial(5 - amount3 - amount2) / (math.factorial(3 - amount2) * math.factorial((5 - amount2 - amount3) - (3 - amount3)))
    brelan = math.factorial(2 - amount2) / (math.factorial(2 - amount2) * math.factorial((2 - amount2) - (2 - amount2)))
    res = (pair * brelan) / 6**(5 - amount3 - amount2)
    print("Chances to get a %d full of %d: %.2f%%" % (third, twice, res * 100))

def carre(dice, A):
    res = 0
    for die in dice:
        if res == 0 and die != A:
            res = 1.0 / 6.0
        elif die != A:
            res *= 1.0 / 6.0
    print("Chances to get a %d four-of-a-kind: %.2f%%" % (A, res * 100))

def pair(dice, A):
    res = 0
    for die in dice:
        if res == 0 and die != A:
            res = 1.0 / 6.0
        elif die != A:
            res *= 1.0 / 6.0
    print("Chances to get a %d pair: %.2f%%" % (A, res * 100))

def brelan(dice, A):
    res = 0
    for die in dice:
        if res == 0 and die != A:
            res = 1.0 / 6.0
        elif die != A:
            res *= 1.0 / 6.0
    print("Chances to get a %d brelan: %.2f%%" % (A, res * 100))