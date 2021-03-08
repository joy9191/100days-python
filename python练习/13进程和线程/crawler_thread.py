#!/usr/bin/python
#coding=utf-8

import urllib
from bs4 import BeautifulSoup
import threading
from threading import Thread
import time
import requests
import json
import time

class DownloadHanlder(Thread):

    def __init__(self, q):
        super(DownloadHanlder, self).__init__()
        self.url = url
        self.q = q

    def run(self):
        url = self.q.get()
        result = urllib.urlopen(url)
        r = result.read()
        title = BeautifulSoup(r, "html.parser").find('header', 'title').find('h1').get_text()
        # print "title" + title
        print("title" + title)
        content = BeautifulSoup(r, "html.parser").find('div', 'cnbeta-article-body').find_all('p')
        for texts in content:
            p = texts.get_text()
            # print p
        # cursor = connection.cursor()
        # cursor.execute('insert into cnbeta_information (info_url,info_title,info_content) value (%s,%s,%s)') % [hrefs, title, p]

def addCnbeta():
    html = urllib.urlopen('https://www.cnbeta.com/')   # 抓取网页的源码
    response = html.read()  # 读取文件
    res = BeautifulSoup(response, "html.parser").find_all('a')
    hrefList = []
    for text in res:
        href = text.get('href')
        if href == None:
            continue
        elif 'articles' not in href:
            continue
        elif href.startswith('//'):
            href = 'http:' + href
        hrefList.append(href)
    hrefList = set(hrefList)  # set中的元素是无序的，并且重复元素在set中自动被过滤
    hrefList=list(hrefList) # set转list，并排序
    hrefList.sort() 
    html.close()
    print(len(hrefList))

    start=time.time()
    workQueue = queue.Queue(10)
    threads=[]
    for href in hrefList:
        workQueue.put(href)
        t=DownloadHanlder(workQueue)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print ("退出主线程")
    end=time.time()
    print('Execution time: ', (end - start), 's')


if __name__ == '__main__':
    addCnbeta()
