#!/usr/bin/python
#coding = utf-8

from multiprocessing import Process,Queue
from time import time, sleep

counter = 0


def sub_task(string,q):
    # global counter
    q.put(counter)
    while qsize(q) < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

        
def main():
	q = Queue()
	Process(target=sub_task, args=('Ping', q)).start()
	Process(target=sub_task, args=('Pong', q)).start()


if __name__ == '__main__':
    main()
