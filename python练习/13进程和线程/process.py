#!/usr/bin/python
#coding = utf-8

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(10, 15)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    # target参数为函数名，进程启动要执行的该函数，args是传给该函数的参数，是一个元祖
    p1.start()
    p2.start()
    # start方法用来启动进程
    p1.join()
    p2.join()
    # join方法表示主进程等待子进程执行结束
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()