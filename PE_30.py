import sys
import math

def euler_30():

	ans = []

	for a in range (2,200000):
	
		list_of_ints = [int(i) for i in str(a)]
		list_of_five = [i**5 for i in list_of_ints]
		
		if a == sum(list_of_five):
			ans.append(a)
		
	print ans
	print sum(ans)

if __name__ == "__main__": 
    
    euler_30();
    #print result