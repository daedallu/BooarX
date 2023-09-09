

#!/usr/bin/python -tt
def fac(num):
	factorial=1
	if num == 0:
		pass
	elif num < 0:
		raise Exception("Negative numbers has not factorial.") 
	else:
		for i in range(1, num+1):
			factorial=factorial*i            
	return factorial
