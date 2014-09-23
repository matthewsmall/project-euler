def euler_35():

	total = 0

	for a in range (2,999999):
	
		if isprime(a) <> 1: continue
	
		# turns 123 into [1,2,3,1,2,3]
		list_of_ints = [int(i) for i in str(a)] * 2
		
		# initializes number of primes for one number to 0
		num_prime = 0
		
		# for each a we check 1 to number of digits in a
		for b in range(1,len(list_of_ints)/2+1):
			
			# get a list starting at b, and going num of digits
			seq = list_of_ints[b:b+len(list_of_ints)/2:1]
			
			# turn that list back into an int
			num = int(''.join(map(str,seq)))
		
			#check if the number is prime, if so, add one to the prime total for this a
			if isprime(num) == 1: 
				num_prime += 1
				#if num_prime ever gets as high as the length of a (ie. all rotations matched) then count it
				if num_prime == len(list_of_ints)/2:
					total += 1
					print(a)
		
	print total

def isprime(n):
    #check if integer n is a prime - range starts with 2 and only needs to go up the squareroot of n
    for x in xrange(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
	
if __name__ == "__main__": 
    
    euler_35();
    #print result
