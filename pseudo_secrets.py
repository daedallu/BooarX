import random as rnd
import os

def choice(list_main):
	LENGTH=len(list_main)
	choice= rnd.randint(0, LENGTH-1)
	return list_main[choice]
	
def token_bytes(size):
	tokenb=os.urandom(size)
	return tokenb
	
	
