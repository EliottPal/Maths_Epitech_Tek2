##
## EPITECH PROJECT, 2020
## 207demography_2019
## File description:
## main
##

import sys
from calc import *

# USAGE
# 	./207demography code [...]
# DESCRIPTION
# 	code    country code

# Diviser les valeurs du csv par 10^6 (millions d'hab)

def checkArguments():
    if len(sys.argv) < 2:
        print("Invalid number of args")
        exit(84)
    for i in sys.argv:
        if i == "./207demography":
            continue
        try:
            if not i.isupper():
                raise
        except:
            print("Invalid Argument")
            exit (84)

def countriesLoop():
    countryList = list()
    for country in sys.argv[1:]:
        countryList.append(country)
    countryInfos(countryList)

def main():
    checkArguments()
    countriesLoop()