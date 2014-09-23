def euler_23():

	limit = 28124
	ab_below = findAbundants(limit)
	
	list = range(limit)
	for x in ab_below:
		for y in ab_below:
			if x + y >= limit: break
			list [x + y] = 0
	
	print(sum(list))
	
def findAbundants(n):
	list_of_ab = []
	for i in range (12,n):
		if sum(list(divisorGenerator(i))) > i: list_of_ab.append(i)
	return list_of_ab
	
def divisorGenerator(n):
    for i in xrange(1,n/2+1):
        if n%i == 0: yield i

if __name__ == "__main__": 
    euler_23();
    #print result
