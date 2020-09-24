##
## EPITECH PROJECT, 2020
## 202unsold_2019
## File description:
## main
##

import sys
import signal
from calc import *

# USAGE
# ./206neutrinos n a h sd
# DESCRIPTION
#   n       number of values
#   a       arithmetic mean
#   h       harmonic mean
#   sd      standard deviation

def checkArguments():
	if len(sys.argv) < 5 or len(sys.argv) > 5:
		print("Invalid number of args")
		exit(84)
	try:
		if not int(sys.argv[1]) or not int(sys.argv[2]) or not int(sys.argv[3]) or not int(sys.argv[4]):
			raise
	except:
		print("Invalid Arguments (numbers expected)")
		exit (84)
	if int(sys.argv[1]) <= 0 or int(sys.argv[2]) <= 0 or int(sys.argv[3]) <= 0 or int(sys.argv[4]) <= 0:
		print("Invalid Arguments (positive numbers expected)")
		exit (84)

def signal_handler(sig, frame):
	exit(0)

def input_loop(values_nb, a_mean, h_mean, deviation):
	value = ""

	while True:
		signal.signal(signal.SIGINT, signal_handler)
		sys.stdout.write("Enter next value: ")
		value = sys.stdin.readline()
		### Error management
		try:
			if (value.rstrip() != "END"):
				int(value.rstrip())
		except ValueError:
			sys.stderr.write("Invalid argument\n")
			exit(0)
		if value.rstrip() == "END":
			exit(0)
		### Calculs
		s_mean = square_mean(float(value), values_nb, a_mean, deviation)
		deviation = standard_deviation(float(value), values_nb, a_mean, deviation)
		a_mean = arithmetic_mean(float(value), values_nb, a_mean)
		h_mean = harmonic_mean(float(value), values_nb, h_mean)
		values_nb += 1
		calc_engine(values_nb, deviation, a_mean, s_mean, h_mean)

def main():
	checkArguments()
	values_nb = float(sys.argv[1])
	a_mean = float(sys.argv[2])
	h_mean = float(sys.argv[3])
	deviation = int(sys.argv[4])
	input_loop(values_nb, a_mean, h_mean, deviation)