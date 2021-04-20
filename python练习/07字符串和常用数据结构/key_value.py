#!/usr/bin/python
#coding=utf-8

s = input('请输入要处理的参数：')
s1=s.replace('=',':')
s2=s1.replace('&','\n')

print(s2)