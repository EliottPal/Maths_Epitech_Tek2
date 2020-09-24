##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## main
##

import sys
from algo import jointLaw
from algo import getZLaw
from algo import getEsperance
from algo import getVariance
# a et b entre 20 et 100
#


def checkArguments():
    if len(sys.argv) is not 3:
        print("Invalid number of args")
        exit(84)
    try:
        if int(sys.argv[1]) < 50:
            raise
    except:
        print("Invalid 1st Argument (must be >= 50)")
        exit (84)
    try:
        if int(sys.argv[2]) < 50:
            raise
    except:
        print("Invalid 2nd Argument (must be >= 50)")
        exit (84)

def printAll(a, b):
    part1 = jointLaw(a, b)
    yLaw = [part1[0] + part1[1] + part1[2] + part1[3] + part1[4], part1[5] + part1[6] + part1[7] + part1[8] + part1[9], part1[10] + part1[11] + part1[12] + part1[13] + part1[14], part1[15] + part1[16] + part1[17] + part1[18] + part1[19], part1[20] + part1[21] + part1[22] + part1[23] + part1[24]]
    xLaw = [part1[0] + part1[5] + part1[10] + part1[15] + part1[20], part1[1] + part1[6] + part1[11] + part1[16] + part1[21], part1[2] + part1[7] + part1[12] + part1[17] + part1[22], part1[3] + part1[8] + part1[13] + part1[18] + part1[23], part1[4] + part1[9] + part1[14] + part1[19] + part1[24]]
    xyLaw = (xLaw[0] + xLaw[1] + xLaw[2] + xLaw[3] + xLaw[4] + yLaw[0] + yLaw[1] + yLaw[2] + yLaw[3] + yLaw[4]) / 2
    zLaw = getZLaw(part1)
    espeX = getEsperance(xLaw, [1, 2, 3, 4, 5])
    espeY = getEsperance(yLaw, [1, 2, 3, 4, 5])
    espeZ = espeX + espeY
    variX = getVariance(xLaw, [1, 2, 3, 4, 5])
    variY = getVariance(yLaw, [1, 2, 3, 4, 5])
    variZ = variX + variY
    print("------------------------------------------------------------------------------")
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    print("Y=10\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(part1[0], part1[1], part1[2], part1[3], part1[4], yLaw[0]))
    print("Y=20\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(part1[5], part1[6], part1[7], part1[8], part1[9], yLaw[1]))
    print("Y=30\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(part1[10], part1[11], part1[12], part1[13], part1[14], yLaw[2]))
    print("Y=40\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(part1[15], part1[16], part1[17], part1[18], part1[19], yLaw[3]))
    print("Y=50\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(part1[20], part1[21], part1[22], part1[23], part1[24], yLaw[4]))
    print("X law\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(xLaw[0], xLaw[1], xLaw[2], xLaw[3], xLaw[4], xyLaw))
    print("------------------------------------------------------------------------------")
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100")
    print("p(Z=z)\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f" %(zLaw[0], zLaw[1], zLaw[2], zLaw[3], zLaw[4], zLaw[5], zLaw[6], zLaw[7], zLaw[8]))
    print("------------------------------------------------------------------------------")
    print("expected value of X:\t%.1f" %(espeX))
    print("variance of X:\t\t%.1f" %(variX))
    print("expected value of Y:\t%.1f" %(espeY))
    print("variance of Y:\t\t%.1f" %(variY))
    print("expected value of Z:\t%.1f" %(espeZ))
    print("variance of Z:\t\t%.1f" %(variZ))
    print("------------------------------------------------------------------------------")

def main():
    checkArguments()
    printAll(int(sys.argv[1]), int(sys.argv[2]))
