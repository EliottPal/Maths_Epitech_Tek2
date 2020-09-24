##
## EPITECH PROJECT, 2020
## 207demography_2019
## File description:
## calc
##

import sys
import math
import csv

def gettingCountryInfos(countryCode):
    countries = list()
    inside = list()
    with open("data.csv") as file:
        file_data = list(csv.reader(file, delimiter='\n'))
        for line in file_data:
            for code in countryCode:
                if (line[0].split(';')[1] == code):
                    for i in line[0].split(';'):
                        inside.append(i)
                    countries.append(inside)
                    inside = list()
    if (len(countries) != len(countryCode)):
        print("Your country code is not supported by the data we are sorry!")
        exit(84)
    return countries

def printNames(countries):
    names = ""
    for country in countries:
        if (names == ""):
            names = country[0]
        else:
            names += ", " + country[0]
    print("Country: %s" %(names))


def sumAll(data):
    sumData = float(0)
    for each in data:
        sumData += float(each)
    print(sumData)
    return sumData

def sumSquareAll(data):
    sumSquare = float(0)
    for each in data:
        sumSquare += math.pow(float(each), 2)
    print(sumSquare)
    return sumSquare

def sumBoth(data1, data2):
    sumBoth = float(0)
    for i in range(len(data1)):
        sumBoth += (float(data1[i]) * float(data2[i]))
    return sumBoth

def fitOne(countries, years):
    a = 0
    b = 0

    for country in countries:
        country = country[2:]
        aTop = (sumAll(years) * (sumSquareAll(country)) - (sumAll(country) * sumBoth(country, years)))
        aBot = (len(years) * sumSquareAll(country)) - sumSquareAll(country)
        a = aTop / aBot
        print("A = " + str(a))


def countryInfos(countryCode):
    infos = gettingCountryInfos(countryCode)
    years = list()
    nb = 0
    for year in range(1960, 2018, 1):
        years.append(year)
    printNames(infos)
    print("Fit1")
    print("\tY = %.2f X - %.2f" %(nb, nb))
    print("\tRoot-mean-square deviation:%.2f" %(nb))
    print("\tPopulation in 2050: %.2f" %(nb))
    print("Fit2")
    print("\tX = %.2f Y + %.2f" %(nb, nb))
    print("\tRoot-mean-square deviation: %.2f" %(nb))
    print("\tPopulation in 2050: %.2f" %(nb))
    print("Correlation: %.4f" %(nb))