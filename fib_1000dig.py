import sys
import math

def fib_1000dig():

	a, b = 0, 1
	
	while a < 1000:

		a, b = b, a+b
		print a
	
	if int(math.log10(a))+1 >= 1000:
		print a
		break


if __name__ == "__main__": 
    
    fib_1000dig();
    #print result