##
## EPITECH PROJECT, 2020
## 201yams_2019
## File description:
## main
##

import sys
from algo import yams
from algo import straight
from algo import full
from algo import carre
from algo import pair
from algo import brelan

def checkArguments():
    if len(sys.argv) is not 7:
        print("Invalid number of args")
        exit(84)
    for i in range(1, 6):
        try:
            k = int(sys.argv[i])
            if k < 0 or k > 6:
                raise
        except:
            print("Invalid argument")
            exit(84)
        combination = sys.argv[6].split('_')
    if combination[0] != "pair" and combination[0] != "three" and combination[0] != "four" and combination[0] != "full" and combination[0] != "straight" and combination[0] != "yams":
        print("Invalid combination")
        exit (84)
    try:
        if not combination[1]:
            raise
    except:
        print("Combination without argument")
        exit (84)
    if combination[1] != '1' and combination[1] != '2' and combination[1] != '3' and combination[1] != '4' and combination[1] != '5' and combination[1] != '6':
        print("Argument must be a number between 1 and 6")
        exit (84)
    if combination[0] == "straight":
        if combination[1] != '5' and combination[1] != '6':
            print("Straight: invalid argument")
            exit (84)
    if combination[0] == "full":
        try:
            if combination[1] and combination[2]:
                if int(combination[1]) == int(combination[2]):
                    raise
        except:
            print("Full: combination with the same numbers")
            exit (84)
        try:
            if int(combination[2]) < 1 or int(combination[2]) > 6:
                raise
        except:
            print("Full: invalid second argument")
            exit (84)
    if combination[0] == "pair" or combination[0] == "yams" or combination[0] == "four":
        if len(sys.argv[6]) != 6:
            print("Invalid combination argument")
            exit (84)
    if combination[0] == "full":
        if len(sys.argv[6]) != 8:
            print("Invalid combination argument")
            exit (84)
    if combination[0] == "three":
        if len(sys.argv[6]) != 7:
            print("Invalid combination argument")
            exit (84)
    if combination[0] == "straight":
        if len(sys.argv[6]) != 10:
            print("Invalid combination argument")
            exit (84)



def main():
    checkArguments()
    dice = list()
    dice.append(int(sys.argv[1]))
    dice.append(int(sys.argv[2]))
    dice.append(int(sys.argv[3]))
    dice.append(int(sys.argv[4]))
    dice.append(int(sys.argv[5]))
    which = sys.argv[6].split('_');
    if (which[0] == "pair"):
        pair(dice, int(which[1]))
    if (which[0] == "three"):
        brelan(dice, int(which[1]))
    if (which[0] == "four"):
        carre(dice, int(which[1]))
    if (which[0] == "full"):
        full(dice, int(which[1]), int(which[2]))
    if (which[0] == "straight"):
        straight(dice, int(which[1]))
    if (which[0] == "yams"):
        yams(dice, int(which[1]))

