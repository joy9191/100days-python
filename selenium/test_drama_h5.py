#!usr/bin/python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest


class TestMy:
    mobile_emulation = {"deviceName": "iPhone 6"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument('--start-maximized') # 最大化窗口
    # options.add_argument('--incognito')  # 隐身模式（无痕模式）
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    driver = webdriver.Chrome(options=options)

    driver.get('https://lingxi.mgtv.com/test/larp/index.html#/home')
    # driver.maximize_window()
    time.sleep(5)

    def test_my_login(self):
        _driver = self.driver
        _driver.find_elements_by_class_name('larp-tab-bar-item')[3].find_element_by_tag_name('i').click()
        time.sleep(5)
        title = _driver.find_element_by_class_name('fixed-header-title').text
        assert title == '我的'
        time.sleep(5)

        _driver.find_element_by_class_name('mine__content-user-unlogin').find_element_by_tag_name('span').click()
        t = _driver.find_element_by_class_name('header-white').find_element_by_tag_name('p').text
        time.sleep(5)
        assert t == '手机验证码登录'
        time.sleep(2)

        _driver.find_element_by_class_name('login-tab').click()
        time.sleep(5)

        _driver.find_element_by_xpath("//input[@type='email']").send_keys('18674831947')
        _driver.find_element_by_xpath("//input[@type='password']").send_keys('qqqqqq')
        _driver.find_element_by_class_name('v3-sect').click()
        _driver.find_element_by_class_name('mgui-btn').click()
        time.sleep(5)

        user = _driver.find_element_by_class_name('mine__content-user-logined').find_element_by_tag_name('div').text
        print(user)
        assert  user == 'mg182330'

    def test_my_order(self):
        _driver = self.driver
        _driver.find_element_by_class_name('order').click()
        time.sleep(5)


