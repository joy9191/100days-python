#!/usr/bin/python
#coding=utf-8

import urllib
from bs4 import BeautifulSoup
from django.db import connection

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
    print len(hrefList)
    html.close()

    db = MySQLdb.connect("127.0.0.1", "root", "", "test", charset='utf8' )
    print '连接数据库成功'
    conn = db.cursor()

    for hrefs in hrefList:
    	print hrefs
        result = urllib.urlopen(hrefs)
        r = result.read()
        title = BeautifulSoup(r, "html.parser").find('header', 'title').find('h1').get_text()
        # print "title" + title
        content = BeautifulSoup(r, "html.parser").find('div', 'cnbeta-article-body').find_all('p')
        # print "content"
        for texts in content:
            p = texts.get_text()
            print p
        # cursor = connection.cursor()
        # cursor.execute('insert into cnbeta_information (info_url,info_title,info_content) value (%s,%s,%s)') % [hrefs, title, p]
        conn.execute('insert into blogs_blog (title,content) value (%s,%s)') % [title, p]

        # print '-------------------------'    
	db.commit()
	conn.close()
	db.close()

if __name__ == '__main__':
	addCnbeta()