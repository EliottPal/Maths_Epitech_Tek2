##
## EPITECH PROJECT, 2020
## 208dowels_2019
## File description:
## main
##

import sys
from algo import *

# USAGE.
# 	/208dowels O0 O1 O2 O3 O4 O5 O6 O7 O8
# DESCRIPTION
# 	Oi   size of the observed class


def checkArguments():
	if len(sys.argv) < 10 or len(sys.argv) > 10:
		print("Invalid number of args")
		exit(84)
	for i in sys.argv:
		if i == "./208dowels":
			continue
		try:
			if int(i) == 0:
				continue
			if not int(i):
				raise
		except:
			print("Invalid Argument (number excpected)")
			exit (84)
		if int(i) < 0:
			print("Invalid Argument (positive number excpected)")
			exit (84)

def main():
	checkArguments()
	params = sys.argv[1:10]
	algo(params)