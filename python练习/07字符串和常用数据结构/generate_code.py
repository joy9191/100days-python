#!/usr/bin/python
import random

def generate_code(code_num=4):
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	code=''

	for i in range(code_num):
		random_code=random.choice(all_chars)
		code+=random_code
	return code

if __name__ == '__main__':
	g=generate_code()
	print g