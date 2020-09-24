##
## EPITECH PROJECT, 2020
## 209poll_2019
## File description:
## calc
##

import math

def calcVariance(N, n, p):
    pval = p / 100
    variance = (pval) * (1 - (pval))
    left = float(N - n)
    right = float(N - 1)
    both = float(left / right)
    both = float((variance / n) * both)
    return both

## CALCUL 95% INTERVAL
## the 95% confidence interval amplitude is 2*1.96SquareRoot(variance)
def calcFirstInterval(variance, votingPercent):
    differ = 1.96 * (math.sqrt(variance) * 100)
    lowerBound = votingPercent - differ
    upperBound = votingPercent + differ

    if (lowerBound < 0):
        lowerBound = 0
    if (upperBound > 100):
        lowerBound = 100

    print("95%% confidence interval:\t[%.2f%%; %.2f%%]" %(lowerBound, upperBound))

## CALCUL 99% INTERVAL
## the 99% confidence interval amplitude is 2*2.58SquareRoot(variance)
def calcSecondInterval(variance, votingPercent):
    differ = 2.58 * (math.sqrt(variance) * 100)
    lowerBound = votingPercent - differ
    upperBound = votingPercent + differ

    if (lowerBound < 0):
        lowerBound = 0
    if (upperBound > 100):
        lowerBound = 100

    print("99%% confidence interval:\t[%.2f%%; %.2f%%]" %(lowerBound, upperBound))

def printAll(popSize, sampleSize, votingPercent):
    variance = calcVariance(popSize, sampleSize, votingPercent)

    print("Population size:\t\t%d" %(popSize))
    print("Sample size:\t\t\t%d" %(sampleSize))
    print("Voting intentions:\t\t%.2f%%" %(votingPercent))
    print("Variance:\t\t\t%.6f" %(variance))
    calcFirstInterval(variance, votingPercent)
    calcSecondInterval(variance, votingPercent)