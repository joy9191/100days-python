#!usr/bin/python
#coding=utf-8

d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
l = sorted(d.items(), key = lambda kv:(kv[1], kv[0]))
# l是个由元祖组成的list，元祖也是一个序列，所以可以通过索引来取对应位置的值

# python 2
# print '按值排序：'
# print l
# print '按键排序：'
# print sorted(d.items())

# python 3
print('按值排序：')
print(l)
print('按键排序：')
print(sorted(d.items()))

di={}
for i in l:
	di[i[0]]=i[1]
# print di
print(di)
	