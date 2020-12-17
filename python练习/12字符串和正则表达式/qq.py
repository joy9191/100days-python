#!/usr/bin/python
#coding=utf-8

import re,time

def main():
	# python2中input()希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来例如”joy“，否则它会引发一个 SyntaxError,
	# 所以一般情况下都是用raw_input() 来读取字符串,python3的input()是标准输入数据，返回为 string 类型，所以python3可以直接使用input()
	username = raw_input('请输入用户名:')
	qq = raw_input('请输入QQ号：')
	# 字符串前加了r，是使用了“原始字符串”的写法，即字符串中没有转义字符
	# /w用来匹配字母/数字/下划线
	# m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username))
	m1 = re.match(r'^\w{6,20}$', username)
	if not m1:
		print '请输入有效的用户名.'
	m2 = re.match(r'^[1-9]\d{4,11}$', qq)
	if not m2:
		print '请输入有效的QQ号.'

	if m1 and m2:
		print '你输入的信息是有效的!'

# 装饰器
def run_time(func):
    def wrapper(n):
        start = time.time()
        func(n)                  # 函数在这里运行
        end = time.time()
        cost_time = end - start
        print "func three run time {}".format(cost_time)
        return cost_time
    return wrapper

# @run_time
def fun_one(n):
    time.sleep(n)

if __name__ == '__main__':
	print run_time(fun_one)(1)