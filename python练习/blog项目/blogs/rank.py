#!/usr/bin/python
#coding=utf-8

import imp
from itertools import count
from django.core.cache import cache
from django_redis import get_redis_connection
from redis import Redis
from django.shortcuts import redirect,render
from models import BlogMsg
from django.core import serializers

rds = Redis(host='127.0.0.1', port=6379)

def get_top_n_blogs(request,n=99):
    c = rds.zrevrange('user_clicks',0,n,withscores=True) #倒序排行
    data=[]
    for i in c:
        d = {}
        bid = int(i[0])
        d['bid'] = bid
        d['read_count'] = int(i[1])
        d['title']=list(BlogMsg.objects.filter(id=bid).values('title'))[0]['title']
        data.append(d)
    print(data)
    return render(request, "rank.html",{'data':data})

def record_click(blog_id,count=1):
    rds.zincrby('user_clicks',count,blog_id)
    v = rds.zscore('user_clicks',blog_id)
    return int(v)


# 参考
# https://blog.csdn.net/weixin_43275654/article/details/109649161
# https://blog.csdn.net/weixin_43692357/article/details/90446593