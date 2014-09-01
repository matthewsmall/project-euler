# project Euler 27
#09/01/2014
# Matthew Small (mattsmall89@gmail.com)

import sys

def is_prime_producing(a,b):
	n = 0
	while isPrime(n**2 + int(a)*n + int(b)):
		n += 1
	return n
	#print "a=" + str(a) + ", b=" + str(b) + ", n=" + str(n) + ", ANS = " + str(int(a)*int(b))

def isPrime(n):
#precondition n is a nonnegative integer
#postcondition:  return True if n is prime and False otherwise.
    if n < 2: 
         return False;
    if n % 2 == 0:
         # return False
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

if __name__ == '__main__':

	most = 0
	for a in range (-999,999):
		for b in range (-999,999):

			challenger = is_prime_producing(a,b)
			
			if challenger > most:
				most = challenger
				final_answer = int(a)*int(b)

	print final_answer