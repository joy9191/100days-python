#!usr/bin/python
# coding=utf-8

from selenium import webdriver
import time
import pytest


class TestScript:
    driver = webdriver.Chrome('D:/Chromedriver/chromedriver.exe')
    driver.get('http://larp.api.mgtv.com/oss')
    driver.maximize_window()

    # 登录
    driver.find_element_by_name('form-username').send_keys('18674831947')
    driver.find_element_by_id('form-password').send_keys('12345678')
    driver.find_element_by_class_name("m-b").click()
    time.sleep(5)

    print('剧本管理')

    def test_login(self):
        login_name = self.driver.find_element_by_class_name("user-info_txt")
        assert login_name.text == '你好，周玖怡'
        print(login_name.text)
        time.sleep(2)

    def test_script_search(self):
        _driver = self.driver
        # 查询&筛选
        # 剧本名称
        _driver.find_elements_by_class_name('el-form-item')[0].click()
        _driver.find_elements_by_class_name('el-form-item')[0].find_element_by_class_name('el-input__inner').send_keys(
            'mumu')
        _driver.find_elements_by_class_name('el-form-item')[4].click()
        time.sleep(5)
        search_result = \
        _driver.find_element_by_class_name('el-table__body-wrapper').find_elements_by_class_name('el-table__row')[
            0].find_element_by_class_name('el-table_1_column_2').find_element_by_class_name('cell')
        assert search_result.text == '582'

        # 剧本状态
        # _driver.find_elements_by_class_name('el-form-item')[1].click()
    driver.quit()


class TestApplyScript:
    driver = webdriver.Chrome('D:/Chromedriver/chromedriver.exe')
    driver.get('http://larp.api.mgtv.com/oss')
    driver.maximize_window()

    # 登录
    driver.find_element_by_name('form-username').send_keys('18674831947')
    driver.find_element_by_id('form-password').send_keys('12345678')
    driver.find_element_by_class_name("m-b").click()
    time.sleep(5)
    driver.find_element_by_link_text('申请剧本管理').click()
    time.sleep(5)

    def test_apply_search(self):
        print('申请剧本管理')
        _driver = self.driver
        # 查询&筛选
        # 剧本名称
        _driver.find_elements_by_class_name('el-form-item')[3].click()
        time.sleep(5)
        d=_driver.find_elements_by_class_name('el-select-dropdown')[0].find_element_by_tag_name('ul').find_element_by_xpath("//span[contains('待处理')]").click()
        print(d)
        # _driver.find_elements_by_class_name('el-form-item')[3].find_element_by_class_name('el-input__inner').send_keys('mumu')
        # _driver.find_elements_by_class_name('el-form-item')[4].click()
        time.sleep(5)
        # search_result=_driver.find_element_by_class_name('el-table__body-wrapper').find_elements_by_class_name('el-table__row')[0].find_element_by_class_name('el-table_1_column_2').find_element_by_class_name('cell')
        # assert search_result.text == '582'
