#!/usr/bin/python
#coding=utf-8

num=int(input('请输入一个正整数：'))
is_prime=True
for i in range(2,num-1):
	if num%i==0:
		is_prime=False
		break
	else:
		is_prime=True
print is_prime