#Project Euler 40
#09/01/2014
#Matthew Small (mattsmall89@gmail.com)
# Project Euler 44
# this is embarrasingly brute force.  definitely coming back to this later.

#!/usr/bin/python

import math
import sys

def Pentagon(n):

	pent_list = [0]

	for i in range(1,int(n)):
		pent_list[len(pent_list):] = [int(i)*(3*int(i)-1)/2]
		#print pent_list[i]

	for i in range(1,int(n)):
		for j in range(1,int(n)):
			if pent_list.count(pent_list[i] - pent_list[j]) > 0:
				if pent_list.count(pent_list[i] + pent_list[j]) > 0:
					if pent_list[i] != pent_list[j]:
						print "D: " + str(abs(pent_list[j] - pent_list[i]))
						print "j: " + str(pent_list[j])
						print "i: " + str(pent_list[i])
						sys.exit(0)

if __name__ == '__main__':
	
	Pentagon(sys.argv[1])
	#arugment of 10000