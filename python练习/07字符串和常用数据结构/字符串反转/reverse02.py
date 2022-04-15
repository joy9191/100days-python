#!/usr/bin/python
# coding=utf-8
n = input("请输入字符串：")


# 方法1 倒序切片
a0=n
# a0 = n[::-1]
print(a0[::-1])

b = ''
for i in a0:
	b += i
print(b)
print(n)
print(id(n))
print(id(b))
print(id(a0))