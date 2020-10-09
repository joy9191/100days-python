#!/usr/bin/python
#coding=utf-8

import urllib2
from bs4 import BeautifulSoup
from django.db import connection
import random
import MySQLdb

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

def geturl(url):
    response = urllib2.Request(url)
    # 网站做了简单的反爬虫机制，请求体中未带浏览器信息会被拦截，直接get请求会被拦截报403，基于这一点，请求时添加User-Agent伪装成浏览器请求，就能访问了
    response.add_header('User-Agent', random.choice(my_headers))
    response = urllib2.urlopen(response)
    return response

def getOushen(url):
    # 打开首页，获取文章链接
    r = geturl(url)
    oushen = r.read()

    res = BeautifulSoup(oushen, "html.parser").find_all('div','placeholder')
    hrefList = []
    for text in res:
        href = text.find('a').get('href')
        if href == None:
            continue
        hrefList.append(href)
    hrefList = set(hrefList)  # set中的元素是无序的，并且重复元素在set中自动被过滤
    # print len(hrefList)

    db = MySQLdb.connect("127.0.0.1", "root", "", "test", charset='utf8' )
    print '连接数据库成功'
    conn = db.cursor()

    for href in hrefList:
    	print href
        result = geturl(href)
        r = result.read()
        html = BeautifulSoup(r, "html.parser")
        title = html.find('h1', 'entry-title').get_text()
        title.encode('utf8')
        print title
        # print "title" 
        content = html.find('div','entry-content').find_all('span')
        # print "content"
        cont = []
        for texts in content:
            p = texts.get_text()
            # p.encode('utf8')
            cont.append(p)
            p = ''.join(cont)
        author = 'oushen'
        blog_sql = 'insert into blogs_blogmsg (title,content,author) values (%s,%s,%s)'
        param = [title, p, author]
        conn.execute(blog_sql,param)
    db.commit()
    conn.close()
    db.close()

def getAll(pages):
    for i in range(1,pages):
        url = 'http://lazymovie.me/oushenwenji/page/'+str(i)
        print url
        getOushen(url)

if __name__ == '__main__':
	getAll(10)