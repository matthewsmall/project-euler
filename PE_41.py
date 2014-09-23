#Project Euler 41
#09/01/2014
#Matthew Small (mattsmall89@gmail.com)

#!/usr/bin/python

# import numpy
import math
import sys

def digit_factorial(n):
	df = str(n)
	length = len(df)
	total = 0

	for i in range(0,length):
		total += math.factorial(int(df[i]))
		
	if int(total) == int(n):
		return True
		#print str(n) + " is a digit factorial!"


if __name__ == '__main__':
	
	for i in range(145,10000000):
		if digit_factorial(i):
			print i