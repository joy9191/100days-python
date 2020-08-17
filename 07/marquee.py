#!/usr/bin/python
#coding=utf-8

import os
import time

def main():
	content = '王格林大胖子王格林大胖子'
	while True:
		os.system('clear')
		print(content)
		time.sleep(0.5)
		content = content.decode('utf-8')[1:].encode('utf-8')+ content.decode('utf-8')[0].encode('utf-8')

if __name__ == '__main__':
	main()