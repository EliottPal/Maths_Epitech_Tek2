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
    print("Average return time: %s" %(nb))
    print("Standard deviation: %s" %(nb))
    print("Time after which 50%% of the ducks are back: %s" %(nb))
    print("Time after which 99%% of the ducks are back: %s" %(nb))
    print("Percentage of ducks back after 1 minute: %s" %(nb))
    print("Percentage of ducks back after 2 minutes: %s" %(nb))
