#!/usr/bin/python

for i in range(5):
	for _ in range(i+1):
		print '*',
	print 

for i in range(5):
	for j in range(5+1):
		if j<5-i:
			print ' ',
		else:
			print '*',
	print

for i in range(5):
	for j in range(5-i-1):
		print ' ',
	for j in range(2*i+1):
		print '*',
	print