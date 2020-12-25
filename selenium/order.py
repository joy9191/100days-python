#!usr/bin/python
#coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://item.jd.com/100012043978.html')  # 打开百度
driver.find_element_by_link_text(u'你好，请登录').click()
driver.find_element_by_link_text(u'账户登录').click()
driver.find_element_by_name('loginname').send_keys('18674831947')
driver.find_element_by_name('nloginpwd').send_keys('joy@040312')
driver.find_element_by_id('loginsubmit').click()
driver.find_element_by_id('btn-reservation').click()