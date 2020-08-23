#!/usr/bin/python
#coding=utf-8

from functools import wraps

def logit(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		print(func.__name__+' was called')
		# 这一句是返回了什么
		return func(*args, **kwargs)
	return with_logging

def log(logfile='first.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			print(func.__name__+' was called')
			# 'a',追加，将内容写入到已有文件的末尾
			with open(logfile,'a') as f:
				f.write(func.__name__+' was called')
			return func(*args, **kwargs)
		return wrapped_function
	return logging_decorator

@logit
def func1():
	pass

@log()
def func2():
	pass

def main():
	func2()
	func1()

if __name__ == '__main__':
	main()