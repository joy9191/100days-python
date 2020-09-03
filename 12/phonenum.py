#!/usr/bin/python
#coding=utf-8

import re

def main():
	pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
	sentence = '''
	重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
	'''
	result1 = pattern.findall(sentence)
	print result1

	for result2 in pattern.finditer(sentence):
		print result2.group()



if __name__ == '__main__':
	main()