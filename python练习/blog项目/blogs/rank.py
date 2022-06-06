#!/usr/bin/python
#coding=utf-8

from django.core.cache import cache

def get_top_n_blogs():
    cache.set('i','61', 60*60)
    c = cache.get('i')
    return c

def record_click():
    pass