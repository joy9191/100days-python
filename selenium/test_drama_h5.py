#!usr/bin/python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest
import logging


class TestMy:
    mobile_emulation = {"deviceName": "iPhone 6"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument('--start-maximized') # 最大化窗口
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    # options.add_argument(r"user-data-dir=C:\Users\KLYG\AppData\Local\Google\Chrome\User Data")
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    driver = webdriver.Chrome(options=options)

    driver.get('https://lingxi.mgtv.com/test/larp/index.html#/home')
    time.sleep(5)
    log = logging.getLogger(__name__)
    log.info("logging information")

    def test_my_login(self):
        """
        进入我的页面并登录
        """
        _driver = self.driver
        _driver.find_elements_by_class_name('larp-tab-bar-item')[3].find_element_by_tag_name('i').click()
        time.sleep(5)
        title = _driver.find_element_by_class_name('fixed-header-title').text
        pytest.assume(title == '我的')
        self.log.info("顶部标题为： {0}".format(title))
        time.sleep(5)

        _driver.find_element_by_class_name('mine__content-user-unlogin').find_element_by_tag_name('span').click()
        t = _driver.find_element_by_class_name('header-white').find_element_by_tag_name('p').text
        time.sleep(5)
        pytest.assume(t == '手机验证码登录')
        self.log.info("顶部标题为： {0}".format(t))
        time.sleep(2)

        _driver.find_element_by_class_name('login-tab').click()
        time.sleep(5)

        _driver.find_element_by_xpath("//input[@type='email']").send_keys('15388043397')
        _driver.find_element_by_xpath("//input[@type='password']").send_keys('111111')
        _driver.find_element_by_class_name('v3-sect').click()
        _driver.find_element_by_class_name('mgui-btn').click()
        time.sleep(5)

        user = _driver.find_element_by_class_name('mine__content-user-logined').find_element_by_tag_name('div').text
        print(user)
        pytest.assume(user == '15388043397', '登录账号不对')

    def test_my_order(self):
        """
        查看我的订单信息
        """
        _driver = self.driver
        _driver.find_element_by_class_name('order').click()
        time.sleep(5)

        pytest.assume(_driver.find_elements_by_class_name('order_list_item')[0].find_element_by_class_name(
            'name').text == '芒果城0125 拼队')
        pytest.assume(_driver.find_elements_by_class_name('order_list_item')[0].find_element_by_class_name(
            'status').text == '待使用', '状态不对')
        pytest.assume(_driver.find_elements_by_class_name('order_list_item')[0].find_element_by_class_name(
            'order_list_item_content_button').text == '查看券码')

        # 切换到待支付
        tab1 = _driver.find_elements_by_xpath("//section[@class='order_tap_item']")[0]
        print(tab1.text)
        tab1.click()
        time.sleep(5)
        order_result = _driver.find_element_by_class_name('van-list__finished-text').text
        print(order_result)
        pytest.assume(order_result == '暂无更多订单!')

        # 切换到待使用
        tab2 = _driver.find_elements_by_xpath("//section[@class='order_tap_item']")[1]
        print(tab2.text)
        tab2.click()
        time.sleep(5)

        # 进入订单详情页
        _driver.find_elements_by_class_name('order_list_item')[0].click()
        time.sleep(5)

        title = _driver.find_element_by_class_name('fixed-header-title').text
        pytest.assume(title == '订单详情', '未成功跳转到指定页面')
        time.sleep(5)

        open_time = _driver.find_element_by_class_name('price').text
        pytest.assume(open_time == '开场时间:\n2021-04-03 11:00 - 2021-04-03 12:45', '开场时间显示异常')

        refund_rules = _driver.find_element_by_class_name('order_detail_concat_info_merchant_time').text
        # pytest.assume(refund_rules == '退款规则:\n未到达最低开场人数前，可随时退款，拼场成功后不可退款 2021-04-03 '
        #                               '11:00未达到开场最低人数，系统将自动退款\n支付成功后，请在场次时间内使用，逾期将无法使用 ')
        assert refund_rules == '退款规则:\n未到达最低开场人数前，可随时退款，拼场成功后不可退款 2021-04-03 ' \
                               '11:00未达到开场最低人数，系统将自动退款\n支付成功后，请在场次时间内使用，逾期将无法使用 '











