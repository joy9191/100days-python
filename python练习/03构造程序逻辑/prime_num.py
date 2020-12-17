#!/usr/bin/python

is_prime=True
for num in range(2,100):
	for i in range(2,num):
		if num%i==0:
			is_prime=False
			break
		else:
			is_prime=True
	if is_prime==True:
		print num,