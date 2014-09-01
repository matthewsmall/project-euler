#Project Euler 40
#09/01/2014
#Matthew Small (mattsmall89@gmail.com)

#!/usr/bin/python

# import numpy
import math
import sys

def Champernowne(n):

	champ = ""
	
	for i in range(1,int(n)):
		champ = champ + str(i)

	return int(champ[0])*int(champ[9])*int(champ[99])*int(champ[999])*int(champ[9999])*int(champ[99999])*int(champ[999999])

if __name__ == '__main__':
	
	#used function above with some manual work to find minimun length to get 1000000 digits
	print Champernowne(185186)