#!usr/bin/python
#coding=utf-8

from multiprocessing import Process, Queue
from random import randint
from time import time

def task(curr_list,queue):
	total=0
	for number in curr_list:
		total += number
	queue.put(total)

def main():
	# 建一个进程列表
	processes=[]
	index=0
	number_list = [x for x in range(1, 100000001)]
	for i in range(8):
		p=Process(target=task, args=(number_list[index:index+12500000], Queue()))
		index+=12500000
		processes.append(p)
		p.start()

	start = time()
	for p1 in processes:
		p1.join()
	total=0
	while not result_queue.empty():
		total += result_queue.get()
	print(total)
	end = time()
	print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
	main()