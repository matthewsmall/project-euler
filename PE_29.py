import sys
import math

def euler_29():
	
	mylist = []

	for a in range (2,101):
		for b in range (2,101):
		
			mylist.append(a**b)

	# print set(mylist)
	print len(set(mylist))

if __name__ == "__main__": 
    
    euler_29();
    #print result