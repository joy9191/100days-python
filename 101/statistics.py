#!/usr/bin/python
#coding=utf-8
import re

with open('101/I have a dream.txt','r') as f:
	line = f.readlines()[0]
	print line

string = re.sub(',',"",line)
print string
