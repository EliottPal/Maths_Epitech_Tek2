##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## main
##

import sys
from algo import *
import time

def checkArguments():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Invalid number of args")
        exit(84)
    try:
        if not int(sys.argv[1]):
            raise
    except:
        print("Invalid 1st Argument (number expected)")
        exit (84)
    if len(sys.argv) == 3:
        try:
            if not int(sys.argv[2]):
                raise
        except:
            print("Invalid 2nd Argument (number expected)")
            exit (84)


def printOption1(combinations, size):
    if (combinations > size):
        print("Don't be dumb i can't find %d combinations in %d. The second number must be greater than the first one" % (combinations, size))
        exit(84)
    print("%d-combinations of a set of size %d:" %(combinations, size))
    print(getCoeff(size, combinations))

def printOption2():
    if float(sys.argv[1]) < 0:
        print("Argument must be positive")
        exit(84);
    toPrint = 42
    debutTime = time.time()
    print("Binomial distribution:")
    print("0 -> %.3f\t1 -> %.3f\t2 -> %.3f\t3 -> %.3f\t4 -> %.3f" %(binomial(float(sys.argv[1]), 0), binomial(float(sys.argv[1]), 1), binomial(float(sys.argv[1]), 2), binomial(float(sys.argv[1]), 3), binomial(float(sys.argv[1]), 4)))
    print("5 -> %.3f\t6 -> %.3f\t7 -> %.3f\t8 -> %.3f\t9 -> %.3f" %(binomial(float(sys.argv[1]), 5), binomial(float(sys.argv[1]), 6), binomial(float(sys.argv[1]), 7), binomial(float(sys.argv[1]), 8), binomial(float(sys.argv[1]), 9)))
    print("10 -> %.3f\t11 -> %.3f\t12 -> %.3f\t13 -> %.3f\t14 -> %.3f" %(binomial(float(sys.argv[1]), 10), binomial(float(sys.argv[1]), 11), binomial(float(sys.argv[1]), 12), binomial(float(sys.argv[1]), 13), binomial(float(sys.argv[1]), 14)))
    print("15 -> %.3f\t16 -> %.3f\t17 -> %.3f\t18 -> %.3f\t19 -> %.3f" %(binomial(float(sys.argv[1]), 15), binomial(float(sys.argv[1]), 16), binomial(float(sys.argv[1]), 17), binomial(float(sys.argv[1]), 18), binomial(float(sys.argv[1]), 19)))
    print("20 -> %.3f\t21 -> %.3f\t22 -> %.3f\t23 -> %.3f\t24 -> %.3f" %(binomial(float(sys.argv[1]), 20), binomial(float(sys.argv[1]), 21), binomial(float(sys.argv[1]), 22), binomial(float(sys.argv[1]), 23), binomial(float(sys.argv[1]), 24)))
    print("25 -> %.3f\t26 -> %.3f\t27 -> %.3f\t28 -> %.3f\t29 -> %.3f" %(binomial(float(sys.argv[1]), 25), binomial(float(sys.argv[1]), 26), binomial(float(sys.argv[1]), 27), binomial(float(sys.argv[1]), 28), binomial(float(sys.argv[1]), 29)))
    print("30 -> %.3f\t31 -> %.3f\t32 -> %.3f\t33 -> %.3f\t34 -> %.3f" %(binomial(float(sys.argv[1]), 30), binomial(float(sys.argv[1]), 31), binomial(float(sys.argv[1]), 32), binomial(float(sys.argv[1]), 33), binomial(float(sys.argv[1]), 34)))
    print("35 -> %.3f\t36 -> %.3f\t37 -> %.3f\t38 -> %.3f\t39 -> %.3f" %(binomial(float(sys.argv[1]), 35), binomial(float(sys.argv[1]), 36), binomial(float(sys.argv[1]), 37), binomial(float(sys.argv[1]), 38), binomial(float(sys.argv[1]), 39)))
    print("40 -> %.3f\t41 -> %.3f\t42 -> %.3f\t43 -> %.3f\t44 -> %.3f" %(binomial(float(sys.argv[1]), 40), binomial(float(sys.argv[1]), 41), binomial(float(sys.argv[1]), 42), binomial(float(sys.argv[1]), 43), binomial(float(sys.argv[1]), 44)))
    print("45 -> %.3f\t46 -> %.3f\t47 -> %.3f\t48 -> %.3f\t49 -> %.3f" %(binomial(float(sys.argv[1]), 45), binomial(float(sys.argv[1]), 46), binomial(float(sys.argv[1]), 47), binomial(float(sys.argv[1]), 48), binomial(float(sys.argv[1]), 49)))
    print("50 -> %.3f" %(binomial(float(sys.argv[1]), 50)))
    print("Overload: %.1f%%" % (getOverloadBino(float(sys.argv[1]))))
    print("Computation time: %.2f ms" %(time.time() - debutTime))

    debutTime = time.time()
    print("\nPoisson distribution:")
    print("0 -> %.3f\t1 -> %.3f\t2 -> %.3f\t3 -> %.3f\t4 -> %.3f" %(poisson(float(sys.argv[1]), 0), poisson(float(sys.argv[1]), 1), poisson(float(sys.argv[1]), 2), poisson(float(sys.argv[1]), 3), poisson(float(sys.argv[1]), 4)))
    print("5 -> %.3f\t6 -> %.3f\t7 -> %.3f\t8 -> %.3f\t9 -> %.3f" %(poisson(float(sys.argv[1]), 5), poisson(float(sys.argv[1]), 6), poisson(float(sys.argv[1]), 7), poisson(float(sys.argv[1]), 8), poisson(float(sys.argv[1]), 9)))
    print("10 -> %.3f\t11 -> %.3f\t12 -> %.3f\t13 -> %.3f\t14 -> %.3f" %(poisson(float(sys.argv[1]), 10), poisson(float(sys.argv[1]), 11), poisson(float(sys.argv[1]), 12), poisson(float(sys.argv[1]), 13), poisson(float(sys.argv[1]), 14)))
    print("15 -> %.3f\t16 -> %.3f\t17 -> %.3f\t18 -> %.3f\t19 -> %.3f" %(poisson(float(sys.argv[1]), 15), poisson(float(sys.argv[1]), 16), poisson(float(sys.argv[1]), 17), poisson(float(sys.argv[1]), 18), poisson(float(sys.argv[1]), 19)))
    print("20 -> %.3f\t21 -> %.3f\t22 -> %.3f\t23 -> %.3f\t24 -> %.3f" %(poisson(float(sys.argv[1]), 20), poisson(float(sys.argv[1]), 21), poisson(float(sys.argv[1]), 22), poisson(float(sys.argv[1]), 23), poisson(float(sys.argv[1]), 24)))
    print("25 -> %.3f\t26 -> %.3f\t27 -> %.3f\t28 -> %.3f\t29 -> %.3f" %(poisson(float(sys.argv[1]), 25), poisson(float(sys.argv[1]), 26), poisson(float(sys.argv[1]), 27), poisson(float(sys.argv[1]), 28), poisson(float(sys.argv[1]), 29)))
    print("30 -> %.3f\t31 -> %.3f\t32 -> %.3f\t33 -> %.3f\t34 -> %.3f" %(poisson(float(sys.argv[1]), 30), poisson(float(sys.argv[1]), 31), poisson(float(sys.argv[1]), 32), poisson(float(sys.argv[1]), 33), poisson(float(sys.argv[1]), 34)))
    print("35 -> %.3f\t36 -> %.3f\t37 -> %.3f\t38 -> %.3f\t39 -> %.3f" %(poisson(float(sys.argv[1]), 35), poisson(float(sys.argv[1]), 36), poisson(float(sys.argv[1]), 37), poisson(float(sys.argv[1]), 38), poisson(float(sys.argv[1]), 39)))
    print("40 -> %.3f\t41 -> %.3f\t42 -> %.3f\t43 -> %.3f\t44 -> %.3f" %(poisson(float(sys.argv[1]), 40), poisson(float(sys.argv[1]), 41), poisson(float(sys.argv[1]), 42), poisson(float(sys.argv[1]), 43), poisson(float(sys.argv[1]), 44)))
    print("45 -> %.3f\t46 -> %.3f\t47 -> %.3f\t48 -> %.3f\t49 -> %.3f" %(poisson(float(sys.argv[1]), 45), poisson(float(sys.argv[1]), 46), poisson(float(sys.argv[1]), 47), poisson(float(sys.argv[1]), 48), poisson(float(sys.argv[1]), 49)))
    print("50 -> %.3f" %(poisson(float(sys.argv[1]), 50)))
    print("Overload: %.1f%%" % (getOverloadPoisson(float(sys.argv[1]))))
    print("Computation time: %.2f ms" %(time.time() - debutTime))

def chooseCommand():
    if len(sys.argv) == 3:
        printOption1(int(sys.argv[2]), int(sys.argv[1]))
    if len(sys.argv) == 2:
        printOption2()

def main():
    try:
        checkArguments()
        chooseCommand()
    except ValueError:
        print ("Something went wrong!")
        exit (84);
