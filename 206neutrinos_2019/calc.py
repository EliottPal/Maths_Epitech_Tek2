##
## EPITECH PROJECT, 2020
## 206neutrinos_2019
## File description:
## calc
##

import sys
import math

def standard_deviation(value, values_nb, a_mean, deviation):
    Vnsq = math.pow(deviation, 2)
    Cn = (Vnsq + math.pow(a_mean, 2)) * values_nb
    Cn += math.pow(value, 2)
    Cn /= values_nb + 1
    Cn -= math.pow(arithmetic_mean(value, values_nb ,a_mean), 2)
    return math.sqrt(Cn)

def arithmetic_mean(value, values_nb, a_mean):
    Cn = float(values_nb * a_mean) + value
    return Cn / (values_nb + 1)

def square_mean(value, values_nb, a_mean, deviation):
    Vnsq = math.pow(deviation, 2)
    Cn = (Vnsq + math.pow(a_mean, 2)) * values_nb
    Cn += math.pow(value, 2)
    res = (1 / (values_nb + 1)) * Cn
    return math.sqrt(res)

def harmonic_mean(value, values_nb, h_mean):
    res = (values_nb + 1) / ((1 / value) + (values_nb / h_mean))
    return res

def calc_engine(values_nb, deviation, a_mean, s_mean, h_mean):
    print("\tNumber of values:\t%d" %(values_nb))
    print("\tStandard deviation:\t%.2f" %(deviation))
    print("\tArithmetic mean:\t%.2f" %(a_mean))
    print("\tRoot mean square:\t%.2f" %(s_mean))
    print("\tHarmonic mean:\t\t%.2f\n" %(h_mean))