#!usr/bin/python
#coding=utf-8

from time import time

def main():
	total = 0
	start=time()
	for i in range(1,100000001):
		total+=i
	print total
	end=time()
	print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
	main()