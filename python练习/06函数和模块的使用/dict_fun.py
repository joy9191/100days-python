#!/usr/bin/python
# coding=utf-8

# 当序列为元组时
foo1 = ('123','adb',456)
# 当序列为字符串时
foo2 = ('hello world!')
# 当序列为字典时
foo3 = {'name':'zjy','sex':'female','age':32}
print(list(foo1)) # ['123', 'adb', 456]
print(list(foo2)) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
print(list(foo3)) # ['name', 'sex', 'age']