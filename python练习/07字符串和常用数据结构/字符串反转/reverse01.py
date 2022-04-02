#!/usr/bin/python
# coding=utf-8
n = input("请输入字符串：")
a='123456789'

# 方法1 倒序切片
a0 = n[::-1]
print(a0)

# 方法2 反转列表法
a1=''.join(reversed(n))
print(a1)

c = list(n)
c.reverse()
a2 = ''.join(c)
print(a2)

# 方法3 遍历索引法
a3=''
for i in n:
	a3 = i + a3
print(a3)

b='hello world'
b =b[::3]
print(b)
