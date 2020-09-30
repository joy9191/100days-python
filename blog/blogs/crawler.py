#!/usr/bin/python
#coding=utf-8

import urllib
from bs4 import BeautifulSoup
import MySQLdb
import requests
import json
import time

def addCnbetaDb():
    html = urllib.urlopen('https://www.cnbeta.com/')   # 抓取网页的源码
    res = html.read()  # 读取文件
    _res = BeautifulSoup(res, "html.parser").find_all('a')
    hrefList = []
    for text in _res:
        href = text.get('href')
        if href == None:
            continue
        elif 'articles' not in href:
            continue
        elif href.startswith('//'):
            href = 'http:' + href
        hrefList.append(href)
    hrefs = hrefList[0]
    # hrefList = set(hrefList)  # set中的元素是无序的，并且重复元素在set中自动被过滤
    html.close()

    db = MySQLdb.connect("127.0.0.1", "root", "", "test", charset='utf8' )
    print '连接数据库成功'
    conn = db.cursor()
    
    url = 'http://47.98.182.254/crawler'
    # for hrefs in hrefList:
    # 	print hrefs
    #     html = urllib.urlopen(hrefs)
    #     result = urllib.urlopen(hrefs)
    #     r = result.read()
    #     title = BeautifulSoup(r, "html.parser").find('header', 'title').find('h1').get_text()
    #     title = title.encode('utf8')
    #     # print type(title)
    #     content = BeautifulSoup(r, "html.parser").find('div', 'cnbeta-article-body').find_all('p')
    #     # print "content"
    #     cont = []
    #     for texts in content:
    #         p = texts.get_text()
    #         cont.append(p)
    #     p = ''.join(cont)
    #     data = {
    #     "title":title,
    #     "content":p,
    #     }
    #     response = requests.post(url, data=data)
    #     print response.status_code
    #     blog_sql = 'insert into blogs_blogmsg (title,content) values (%s,%s)'
    #     param = [title, p]
    #     conn.execute(blog_sql,param)
        # print '-------------------------'  
    result = urllib.urlopen(hrefs)
    r = result.read()
    bs = BeautifulSoup(r, "html.parser")
    title = bs.find('header', 'title').find('h1').get_text()
    title = title.encode('utf8')
    # print type(title)
    content = bs.find('div', 'cnbeta-article-body').find_all('p')
    # print "content"
    cont = []
    for texts in content:
        p = texts.get_text()
        cont.append(p)
    p = ''.join(cont)
    date = bs.find('div', 'meta').find('span').get_text()+':00'
    author = bs.find('div', 'article-author').get_text()
    # _date = time.strftime(date,u'%Y年%m月%d日 %H:%M')
    # strptime字符串格式转化为日期格式,strftime日期格式转化为字符串格式
    _date = time.strptime(date,u'%Y年%m月%d日 %H:%M:%S')
    fdate = time.strftime('%Y-%m-%d %H:%M:%S', _date)
    blog_sql = 'insert into blogs_blogmsg (title,content,date,author) values (%s,%s,%s,%s)'
    param = [title, p, fdate, author]
    conn.execute(blog_sql,param)
    db.commit()
    conn.close()
    db.close()

def addCnbetaApi():
    html = urllib.urlopen('https://www.cnbeta.com/')   # 抓取网页的源码
    res = html.read()  # 读取文件
    _res = BeautifulSoup(res, "html.parser").find_all('a')
    hrefList = []
    for text in _res:
        href = text.get('href')
        if href == None:
            continue
        elif 'articles' not in href:
            continue
        elif href.startswith('//'):
            href = 'http:' + href
        hrefList.append(href)
    # hrefs = hrefList[0]
    hrefList = set(hrefList)  # set中的元素是无序的，并且重复元素在set中自动被过滤
    html.close()
    
    url = 'http://47.98.182.254/crawler'
    for hrefs in hrefList:
    	print hrefs
        html = urllib.urlopen(hrefs)
        result = urllib.urlopen(hrefs)
        r = result.read()
        bs = BeautifulSoup(r, "html.parser")
        title = bs.find('header', 'title').find('h1').get_text()
        title = title.encode('utf8')
        # print type(title)
        content = bs.find('div', 'cnbeta-article-body').find_all('p')
        # print "content"
        cont = []
        for texts in content:
            p = texts.get_text()
            cont.append(p)
        p = ''.join(cont)
        date = bs.find('div', 'meta').find('span').get_text()+':00'
        author = bs.find('div', 'article-author').get_text()
        _date = time.strptime(date,u'%Y年%m月%d日 %H:%M:%S')
        fdate = time.strftime('%Y-%m-%d %H:%M:%S', _date)
        data = {
            "title":title,
            "content":p,
            "date":fdate ,
            "author": author,
        }
        response = requests.post(url, data=data)
        print response.status_code  
    # result = urllib.urlopen(hrefs)
    # r = result.read()
    # bs = BeautifulSoup(r, "html.parser")
    # title = bs.find('header', 'title').find('h1').get_text()
    # title = title.encode('utf8')
    # # print type(title)
    # content = bs.find('div', 'cnbeta-article-body').find_all('p')
    # # print "content"
    # cont = []
    # for texts in content:
    #     p = texts.get_text()
    #     cont.append(p)
    # p = ''.join(cont)
    # date = bs.find('div', 'meta').find('span').get_text()+':00'
    # author = bs.find('div', 'article-author').get_text()
    # # _date = time.strftime(date,u'%Y年%m月%d日 %H:%M')
    # # strptime字符串格式转化为日期格式,strftime日期格式转化为字符串格式
    # _date = time.strptime(date,u'%Y年%m月%d日 %H:%M:%S')
    # fdate = time.strftime('%Y-%m-%d %H:%M:%S', _date)
    # data = {
    #     "title":title,
    #     "content":p,
    #     "date":fdate ,
    #     "author": author,
    # }
    # response = requests.post(url, data=data)
    # print response.status_code
    # blog_sql = 'insert into blogs_blogmsg (title,content) values (%s,%s)'
    # param = [title, p]
    # conn.execute(blog_sql,param)
    # db.commit()
    # conn.close()
    # db.close()


def readHtml(url):
    html = urllib.urlopen('https://www.cnbeta.com/')   # 抓取网页的源码
    response = html.read()

if __name__ == '__main__':
	addCnbetaApi()