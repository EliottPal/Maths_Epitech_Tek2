##
## EPITECH PROJECT, 2020
## 209poll_2019
## File description:
## main
##

import sys
from calc import printAll

# USAGE
# 	./209poll pSize sSize p
# DESCRIPTION
# 	pSize   size of the population
# 	sSize   size of the sample (supposed to be representative)
# 	p       percentage of voting intentions for a specific candidate

def checkArguments():
	if len(sys.argv) < 4 or len(sys.argv) > 4:
		print("Invalid number of args")
		exit(84)
	try:
		if not int(sys.argv[1]) or not int(sys.argv[2]) or not float(sys.argv[3]):
			raise
	except:
		print("Invalid Argument (number expected)")
		exit (84)
	if int(sys.argv[1]) < 0 or int(sys.argv[2]) < 0 or float(sys.argv[3]) < 0:
		print("Invalid Argument (positive number expected)")
		exit (84)
	if int(sys.argv[2]) > int(sys.argv[1]):
		print("Invalid Argument (sample size must be < than population size)")
		exit (84)
	if float(sys.argv[3]) > 100:
		print("Invalid Argument (percent must be < 100)")
		exit (84)

def main():
	checkArguments()
	printAll(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))