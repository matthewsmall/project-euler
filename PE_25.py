import sys
import math

def fib_1000():

	a, b, term = 0, 1, 1
	
	while True:
		a, b = b, a+b
		term += 1
	
		if int(math.log10(b))+1 >= 1000:
			
			print term
			
			with open("euler_25_ans", "w") as f:
				f.write(str(term))
			break

if __name__ == "__main__": 
    
    fib_1000();
    #print result