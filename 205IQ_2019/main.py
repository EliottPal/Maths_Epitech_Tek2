##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## main
##

# USAGE
# ./205IQ u s [IQ1] [IQ2]
# DESCRIPTION
# u       mean
# s       standard deviation
# IQ1     minimum IQ
# IQ2     maximum I

import sys
from algo import *

# Si 4 arguments
# 2e valeur >= a la 1e
# IQ2 > IQ1

def checkArguments():
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        print("Invalid number of args")
        exit(84)
    for i in sys.argv:
        if i == "./205IQ":
            continue
        try:
            if not int(i):
                raise
        except:
            print("Invalid Arguments (numbers expected)")
            exit (84)
    if int (sys.argv[1]) > 200 or int (sys.argv[1]) < 0:
        print("Invalid mu")
        exit (84)
    if len(sys.argv) == 4:
        if int (sys.argv[3]) < 0:
            print("Minimum IQ must be positive")
            exit (84)
        if int (sys.argv[3]) > 200:
            print("Too large IQ")
            exit (84)
    if len(sys.argv) == 5:
        if not int (sys.argv[3]) < int (sys.argv[4]):
            print("Minimum IQ must be < Maximum IQ")
            exit (84)
        if int (sys.argv[3]) < 0:
            print("Minimum IQ must be positive")
            exit (84)
        if int (sys.argv[3]) > 200 or int (sys.argv[4]) > 200:
            print("Too large IQ")
            exit (84)

def main():
    checkArguments()
    if (len(sys.argv) == 3):
        all(int(sys.argv[1]), int(sys.argv[2]))
    if (len(sys.argv) == 4):
        inferior(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    if (len(sys.argv) == 5):
        between(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
