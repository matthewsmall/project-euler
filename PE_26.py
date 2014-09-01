#Project Euler 26
#09/01/2014
#Matthew Small (mattsmall89@gmail.com)

#!/usr/bin/python

# import numpy
# import scipy
# import sys

# def main(num_trials):
# 	print "number of trials: " + num_trials

# 	for i in range(1, int(num_trials)):
# 		#print "i = " + str(i)
# 		print float(1)/i

# if __name__ == "__main__":
# 	main(sys.argv[1])



	#!/usr/bin/env python
def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

longest = max(recurring_cycle(1, i) for i in range(2,1001))
print [i for i in range(2,1001) if recurring_cycle(1, i) == longest][0]