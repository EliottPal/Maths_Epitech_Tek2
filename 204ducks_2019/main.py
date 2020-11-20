##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## main
##

import sys
from algo import *

def checkArguments():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Invalid number of args")
        exit(84)
    try:
        if not float(sys.argv[1]):
            raise
    except:
        print("Invalid 1st Argument (number expected)")
        exit (84)
    if float(sys.argv[1]) < 0 or float(sys.argv[1]) > 2.5:
        print("Invalid number (must be between 0 and 2.5)")
        exit (84)


def main():
    nb = 42
    checkArguments()
    a = float(sys.argv[1])
    ave = average(a)
    print("Standard deviation: %.3f" % standard_deviation(a, ave))
    getTime(a, 0.50)
    getTime(a, 0.99)
    print("Percentage of ducks back after 1 minute: %.1f%%" %(getAmount(a, 1)))
    print("Percentage of ducks back after 2 minutes: %.1f%%" %(getAmount(a, 2)))
