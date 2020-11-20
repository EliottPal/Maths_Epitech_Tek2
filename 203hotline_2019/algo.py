##
## EPITECH PROJECT, 2020
## 203hotline_2019
## File description:
## algo
##

import math

def poisson(length, i):
    p = length / float((8 * 60 * 60))
    lam = 3500 * p
    poisson = (math.exp(-lam)) * (lam**i) / math.factorial(i)
    return poisson

def binomial(length, i):
    p = float(0)
    p = length / float((8 * 60 * 60))
    res = float(0)
    C = math.factorial(3500) / (math.factorial(i) * math.factorial(3500 - i))
    pi = p**i
    p1 = ((1 - p)**(3500 - i))
    res = C * pi * p1
    return res

def getCoeff(x, i):
    a = math.factorial(x)
    ai = math.factorial(i)
    axi = math.factorial(x - i)
    return (a // (ai * axi))

def getOverloadBino(length):
    res = 0
    for i in range(26):
        res += binomial(length, i)
    res = 1 - res;
    res = res * 100
    if (res < 0):
        res = 0
    return res

def getOverloadPoisson(length):
    res = 0
    for i in range(26):
        res += poisson(length, i)
    res = 1 - res;
    res = res * 100
    if (res < 0):
        res = 0
    return res