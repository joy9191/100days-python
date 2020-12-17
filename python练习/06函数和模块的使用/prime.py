#!/usr/bin/python

def is_prime(num):
	is_prime=True
	
	for i in range(2,num-1):
		if num%i==0:
			is_prime=False
			break
		else:
			is_prime=True
		return is_prime