#!/usr/bin/python
# coding=utf-8

#!/usr/bin/python
# coding=utf-8

import itertools

def print_iter(iter):
	for i in iter:
		print(i)


if __name__ == '__main__':
	l=['王','格','林','小','胖','子']
	c = itertools.cycle(l)  # 产生列表的无限循环序列，运行后根本停不下来，只能手动停止
	d = itertools.repeat(l, 3) # 依然是列表的无限循环序列，第二个参数可以控制循环次数
	e = itertools.count(1,2) # 创建一个无限迭代器，默认从0开始，依次+1的自然数迭代器，第二个参数可以配置迭代间隔
	print_iter(e)
