#!/usr/bin/python
# coding=utf-8

def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]  # items[:]创建原始列表的副本,它不引用同一个列表对象。因此，更改li[：]创建的副本不会有更改原始列表的风险。
    print(items)
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

if __name__ == '__main__':
	_items = [1,33,158,5,12,99]
	print(select_sort(_items))