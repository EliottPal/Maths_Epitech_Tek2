##
## EPITECH PROJECT, 2020
## 204ducks_2019
## File description:
## algo
##
import math
import numpy

def f(a, t):
    return a * math.exp(-t) + (4 - 3 * a) * math.exp(t * -2) + (2 * a - 4) * math.exp(t * -4)

def fprime(a, t):
    return -a * math.exp(-t) - (4 - 3 * a) / 2 * math.exp(-2 * t) - (2 * a - 4) / 4 * math.exp(-4 * t)

def average(a):
    res = float(0)
    t = float(0)
    delta = 0.001
    while t < 100:
        res += f(a, t) * t * delta
        t += delta
    min = int(res)
    sec = math.ceil((res - int(res)) * 60)
    print("Average return time: %dm %ds" % (min, sec))
    return res

def standard_deviation(a, average):
    res = float(0)
    t = float(0)
    delta = 0.001
    while t < 100:
        res += f(a, t) * math.pow(t - average, 2)  * delta
        t += delta
    return math.sqrt(res)

def getTime(a, limit):
    t = 0.0
    res = float(0)
    while 1:
        res = fprime(a, t / 60) - fprime(a, 0)
        if res >= limit:
            break
        t += 0.01
    t = int(t)
    min = t / 60
    sec = t - (min * 60)
    print("Time after which %.d%% of the ducks are back: %dm %.2ds" % (limit * 100, min, sec))

def getAmount(a, limit):
    return (fprime(a, limit) - fprime(a, 0)) * 100