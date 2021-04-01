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
        _driver.quit()


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
        # 剧本状态
        _driver.find_elements_by_class_name('el-form-item')[3].click()
        time.sleep(5)
        _driver.find_elements_by_class_name('el-select-dropdown')[2].find_element_by_tag_name('ul').find_elements_by_tag_name('li')[0].click()
        time.sleep(5)
        tr = _driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        for i in tr:
            scrpit_status = i.find_element_by_class_name('el-table_2_column_18').find_element_by_class_name('cell').find_element_by_tag_name('div')
            assert scrpit_status.text == '待处理'
        time.sleep(5)
        _driver.quit()


class TestScriptRecord:
    driver = webdriver.Chrome('D:/Chromedriver/chromedriver.exe')
    driver.get('http://larp.api.mgtv.com/oss')
    driver.maximize_window()

    # 登录
    driver.find_element_by_name('form-username').send_keys('18674831947')
    driver.find_element_by_id('form-password').send_keys('12345678')
    driver.find_element_by_class_name("m-b").click()
    time.sleep(5)
    driver.find_element_by_link_text('剧本演示记录').click()
    time.sleep(5)

    def test_script_record(self):
        print('剧本演示记录')
        _driver = self.driver
        # 查询&筛选
        _driver.find_elements_by_class_name('el-form-item')[0].click()
        _driver.find_elements_by_class_name('el-form-item')[0].find_element_by_class_name('el-input__inner').send_keys(
            '18674831947')
        time.sleep(5)

        search_result = \
            _driver.find_element_by_class_name('el-table__body-wrapper').find_element_by_class_name('el-table__row').find_elements_by_tag_name('td')[1].find_element_by_class_name('cell')
        print(search_result)
        assert search_result.text == '周玖怡'
        time.sleep(5)

    def test_demo_script(self):
        print('演示剧本管理')
        _driver = self.driver
        # 添加剧本
        _driver.find_element_by_class_name('global__button--primary')
