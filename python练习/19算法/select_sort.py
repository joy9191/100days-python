#!/usr/bin/python
# coding=utf-8

def select_sort(items ,comp=lambda x,y:x>y):
	items = items[:]
	for i in range(len(items)-1):
		max_index = i
		for j in range(i+1,len(items)-1):
			if comp(items[j],items[max_index]):
				max_index=j
				print(max_index)
		items[i],items[max_index]=items[max_index],items[i]
	return items

if __name__ == '__main__':
	_items = [1,33,158,5,12,99]
	print(select_sort(_items))