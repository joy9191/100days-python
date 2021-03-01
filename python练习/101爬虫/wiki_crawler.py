#!/usr/bin/python
# coding=utf-8

import urllib
from bs4 import BeautifulSoup
from django.db import connection

def addCnbeta():
    html = urllib.urlopen('https://wiki.imgo.tv/pages/viewpage.action?pageId=23480453')   # 抓取网页的源码
    response = html.read()  # 读取文件
    res = BeautifulSoup(response, "html.parser").find_all('a')
    hrefList = []