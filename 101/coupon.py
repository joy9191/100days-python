#!usr/bin/python
#coding=utf-8

import random

def random_str():
	seed_str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'
	# seed_str = '1'
	res=''
	for x in range(16):
		res=res+random.choice(seed_str)
	return res

def remove_str(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]==l[j]:
				l[i]=-1

def main():
	res_list=[]
	for x in range(200):
		res_list.append(random_str())
	remove_str(res_list)
	i=0
	while i<len(res_list):
		if res_list[i]==-1:
			res_list.remove(res_list[i])
			i-=1
		else:
			i+=1
	print res_list

if __name__ == '__main__':
	main()