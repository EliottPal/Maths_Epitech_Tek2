##
## EPITECH PROJECT, 2020
## 208dowels_2019
## File description:
## algo
##
import sys
import math

def xiSquared(xiSquared, mu):
	tt = [
		 [0.00,0.02,0.06,0.15,0.27,0.45,0.71,1.07,1.64,2.71,3.84,5.41,6.63],
		 [0.02,0.21,0.45,0.71,1.02,1.39,1.83,2.41,3.22,4.61,5.99,7.82,9.21],
		 [0.11,0.58,1.01,1.42,1.87,2.37,2.95,3.66,4.64,6.25,7.81,9.84,11.34],
		 [0.30,1.06,1.65,2.19,2.75,3.36,4.04,4.88,5.99,7.78,9.49,11.67,13.28],
		 [0.55,1.61,2.34,3.00,3.66,4.35,5.13,6.06,7.29,9.24,11.07,13.39,15.09],
		 [0.87,2.20,3.07,3.83,4.57,5.35,6.21,7.23,8.56,10.64,12.59,15.03,16.81],
		 [1.24,2.83,3.82,4.67,5.49,6.35,7.28,8.38,9.80,12.02,14.07,16.62,18.48],
		 [1.65,3.49,4.59,5.53,6.42,7.34,8.35,9.52,11.03,13.36,15.51,18.17,20.09],
		 [2.09,4.17,5.38,6.39,7.36,8.34,9.41,10.66,12.24,14.68,16.92,19.68,21.67],
		 [2.56,4.87,6.18,7.27,8.30,9.34,10.47,11.78,13.44,15.99,18.31,21.16,23.21]
	]
	count = 0
	sys.stdout.write("Fit validity:\t\t")
	for xi in tt[mu - 1]:
		if float(xi) > xiSquared:
			if count == 0:
				sys.stdout.write("P > 99%\n")
				return
			elif count == 12:
				sys.stdout.write("1% < P < 2%\n")
				return
			elif count == 11:
				sys.stdout.write("2% < P < 5%\n")
				return
			elif count == 10:
				sys.stdout.write("5% < P < 10%\n")
				return
			elif count == 9:
				sys.stdout.write("10% < P < 20%\n")
				return
			elif count == 8:
				sys.stdout.write("20% < P < 30%\n")
				return
			elif count == 7:
				sys.stdout.write("30% < P < 40%\n")
				return
			elif count == 6:
				sys.stdout.write("40% < P < 50%\n")
				return
			elif count == 5:
				sys.stdout.write("50% < P < 60%\n")
				return
			elif count == 4:
				sys.stdout.write("60% < P < 70%\n")
				return
			elif count == 3:
				sys.stdout.write("70% < P < 80%\n")
				return
			elif count == 2:
				sys.stdout.write("80% < P < 90%\n")
				return
			elif count == 1:
				sys.stdout.write("90% < P < 99%\n")
				return
		count += 1
	sys.stdout.write("P < 1%\n")

def getP(params):
	p = float(0)
	count = 0
	for i in params:
		p += int(i) * count
		count += 1
	p = p / (100 ** 2)
	return p

def displayFirstPart(classes, params, results):
	sys.stdout.write(" x\t| ")
	for clas in classes:
		if clas == classes[-1]:
			sys.stdout.write("%d+" % (clas[0]))
		elif len(clas) == 1:
			sys.stdout.write("%d" % clas[0])
		else:
			sys.stdout.write("%d-%d" % (clas[0], clas[-1]))
		sys.stdout.write("\t| ")
	sys.stdout.write("Total\n")

	res = 0
	sys.stdout.write(" Ox\t| ")
	for clas in classes:
		for each in clas:
			res += int(params[int(each)])
		sys.stdout.write("%d\t| " % (res))
		res = 0
	sys.stdout.write("100\n")

	sys.stdout.write(" Tx\t| ")
	for result in results:
		sys.stdout.write("%.1f\t| " % result)
	sys.stdout.write("100\n")


def oxMaker(classes, params, res):
	Ox = list()
	res = 0
	for clas in classes:
		for each in clas:
			res += int(params[int(each)])
		Ox.append(res)
		res = 0
	return Ox

def chiSquaredMaker(Ox, Tx):
	chiSquared = float(0)
	for i in range(len(Ox)):
		chiSquared += ((Ox[i] - Tx[i]) ** 2) / Tx[i]
	return chiSquared

def sortArguments():
	classes = []
	check = False
	check_bis = False

	for i in range(1, 10):
		# print(check)
		if int (sys.argv[i]) < 10 and check == False:
			if i < 8 and (int (sys.argv[i]) + int (sys.argv[i + 1]) < 10):
				classes.append([int (i - 1), int (i), int(i + 1)])
				check = True
				check_bis = True
			else:
				# print("GROUP")
				classes.append([int (i - 1), int (i)])
				check = True
		elif i < 9 and int (sys.argv[i]) >= 10 and int (sys.argv[i + 1]) < 10  and int (sys.argv[i + 2]) > 10 and check == False:
			classes.append([int (i - 1), int(i)])
			check = True
		elif check == True and check_bis == True:
			check_bis = False
			continue
		elif check == True and check_bis == False:
			check = False
			continue
		else:
			classes.append([int (i - 1)])
	return classes

def firstPart(params):
	i = 0
	y = float()
	C = 0
	classes = sortArguments()

	res = list()
	p = getP(params)
	for clas in classes:
		y = 0
		for each in clas:
			C = math.factorial(100) / (math.factorial(int(each)) * math.factorial(100 - int(each)))
			y += C * (p ** float(each)) * ((1 - p) ** (100 - float(each)))
		res.append(y * 100)
	y = 0
	for i in res:
		y += i
	print(classes)
	print(params)
	res.append(res.pop() + (100 - y))
	displayFirstPart(classes, params, res)
	Ox = oxMaker(classes, params, res)
	chiSquared = chiSquaredMaker(Ox, res)
	print("Distribution:\t\tB(100, %.4f)" % p)
	print("Chi-squared:\t\t%.3f" % chiSquared)
	print("Degrees of freedom:\t%d" % (len(classes) - 2))
	xiSquared(chiSquared, (len(classes) - 2))

def algo(params):
	firstPart(params)