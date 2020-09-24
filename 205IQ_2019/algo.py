##
## EPITECH PROJECT, 2020
## 205IQ
## File description:
## algo
##

import sys
import math

def f(mu, sigma, x):
    res = (1 / (float(sigma) * math.sqrt(2 * math.pi))) * math.exp(-0.5 * pow((float(x) - float(mu)) / float(sigma), 2))
    return res

def inferior(mu, sigma, x):
    res = float(0)
    delta = 0.01
    i = 0.0
    while i < x:
        res += f(mu, sigma, i)
        i += delta
    print ("%.1f%% of people have an IQ inferior to %d" % (res, x))

def between(mu, sigma, x, y):
    if (x > y):
        exit(84)
    i = x
    res = float(0)
    delta = 0.01
    while i < y:
        res += f(mu, sigma, i)
        i += delta
    print ("%.1f%% of people have an IQ between %d and %d" % (res, x, y))

def all(mu, sigma):
    i = 0
    delta = 1
    res = float(0)
    while i <= 200:
        res = f(mu, sigma, i)
        print("%d %.5f" % (i, res))
        i += delta