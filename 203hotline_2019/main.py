##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## main
##

import sys

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
    print("%s-combinations of a set of size %s:" %(combinations, size))

def printOption2():
    toPrint = 42

    print("Binomial distribution:")
    print("0 -> %.3f\t1 -> %.3f\t2 -> %.3f\t3 -> %.3f\t4 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("5 -> %.3f\t6 -> %.3f\t7 -> %.3f\t8 -> %.3f\t9 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("10 -> %.3f\t11 -> %.3f\t12 -> %.3f\t13 -> %.3f\t14 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("15 -> %.3f\t16 -> %.3f\t17 -> %.3f\t18 -> %.3f\t19 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("20 -> %.3f\t21 -> %.3f\t22 -> %.3f\t23 -> %.3f\t24 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("25 -> %.3f\t26 -> %.3f\t27 -> %.3f\t28 -> %.3f\t29 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("30 -> %.3f\t31 -> %.3f\t32 -> %.3f\t33 -> %.3f\t34 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("35 -> %.3f\t36 -> %.3f\t37 -> %.3f\t38 -> %.3f\t39 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("40 -> %.3f\t41 -> %.3f\t42 -> %.3f\t43 -> %.3f\t44 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("45 -> %.3f\t46 -> %.3f\t47 -> %.3f\t48 -> %.3f\t49 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("50 -> %.3f" %(toPrint))
    print("Overload: %.1f%%" %(toPrint))
    print("Computation time: %.2f ms" %(toPrint))

    print("\nPoisson distribution:")
    print("0 -> %.3f\t1 -> %.3f\t2 -> %.3f\t3 -> %.3f\t4 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("5 -> %.3f\t6 -> %.3f\t7 -> %.3f\t8 -> %.3f\t9 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("10 -> %.3f\t11 -> %.3f\t12 -> %.3f\t13 -> %.3f\t14 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("15 -> %.3f\t16 -> %.3f\t17 -> %.3f\t18 -> %.3f\t19 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("20 -> %.3f\t21 -> %.3f\t22 -> %.3f\t23 -> %.3f\t24 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("25 -> %.3f\t26 -> %.3f\t27 -> %.3f\t28 -> %.3f\t29 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("30 -> %.3f\t31 -> %.3f\t32 -> %.3f\t33 -> %.3f\t34 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("35 -> %.3f\t36 -> %.3f\t37 -> %.3f\t38 -> %.3f\t39 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("40 -> %.3f\t41 -> %.3f\t42 -> %.3f\t43 -> %.3f\t44 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("45 -> %.3f\t46 -> %.3f\t47 -> %.3f\t48 -> %.3f\t49 -> %.3f" %(toPrint, toPrint, toPrint, toPrint, toPrint))
    print("50 -> %.3f" %(toPrint))
    print("Overload: %.1f%%" %(toPrint))
    print("Computation time: %.2f ms" %(toPrint))

def chooseCommand():
    if len(sys.argv) == 3:
        printOption1(sys.argv[2], sys.argv[1])
    if len(sys.argv) == 2:
        printOption2()

def main():
    checkArguments()
    chooseCommand()
