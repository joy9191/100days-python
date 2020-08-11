#!/usr/bin/python

factor_sum=0
for num in range(2,10001):
	for factor in range(1,num):
		if num%factor==0:
			factor_sum+=factor
	if factor_sum==num:
		print 'result is %d'%num
	factor_sum=0
