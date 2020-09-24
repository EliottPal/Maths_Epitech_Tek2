##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## algo
##
from math import *

def formula(a, b, x, y):
    top = (a - x) * (b - y)
    botLeft = (5 * a) - 150
    botRIght = (5 * b) - 150
    bot = botLeft * botRIght
    res = float(top) / float(bot)
    return res

def jointLaw(a, b):
    res = []
    i = 0
    for y in [1, 2, 3, 4, 5]:
        for x in [1, 2, 3, 4, 5]:
            res.append(formula(a, b, x * 10, y * 10))
    return res

def getZLaw(part1):
    i = 1
    start = 0
    zLaw = []
    res = 0

    for x in range(2,11):
        res = 0
        for y in range(i):
            res += part1[start]
            start += 4
        zLaw.append(res)
        start -= 4 * i
        start += 1 if (x < 6) else 5
        i += 1 if (x < 6) else -1
    return zLaw

def getEsperance(Law, ranged):
    res = float(0)

    for y in ranged:
        res += float((y * 10) * (Law[y - 1]))
    return res

def getVariance(Law, ranged):
    res = float(0)
    espe = getEsperance(Law, ranged)

    for i in ranged:
        res += ((i) * 10 - espe) * ((i) * 10 - espe) * Law[i - 1]
    return res