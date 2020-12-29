#!/usr/bin/python
# coding=utf-8

import unittest
from appium import webdriver
import time

class TestSample(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['udid'] = 'R9WNA1RVQYJ'
		desired_caps['appPackage'] = 'com.mg.scriptkilling'
		desired_caps['appActivity'] = 'com.mg.scriptkilling.ui.login.EnterRoomActivity'
		desired_caps['unicodeKeyboard'] = True #使用unicode输入法
		desired_caps['resetKeyboard'] = True  #重置输入法到初始状态
		desired_caps['noReset'] = True  #启动app时不要清除app里的原有的数据
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(10)
		print("start case test")

	def tearDown(self):
		self.driver.quit()
		print("Finish")

	def test_case1(self):
		print("case1")
		# 1+1演示模式
		time.sleep(3)
		self.driver.close_app()
		self.driver.launch_app()
		time.sleep(3)
		# self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button").click()
		print("ok")
		time.sleep(2)

		# 首页
		self.driver.find_element_by_id("com.mg.scriptkilling:id/input_game_coupons_et").send_keys("18674831947")
		time.sleep(2)
		self.driver.find_element_by_id("com.mg.scriptkilling:id/activation_tv").click()
		print("enter")
		time.sleep(3)
		# self.driver.find_element_by_id("com.mg.scriptkilling:id/script_rv")[].find_element_by_id("com.mg.scriptkilling:id/script_poster_iv").click()

		# 演示剧本选择列表页
		self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"叠\")")[0].click()
		time.sleep(2)

		if self.is_element_exist("com.mg.scriptkilling:id/binding_phone_iv"):
			print("True")
		else:
			print("False")
		# a = self.driver.find_element_by_id("com.mg.scriptkilling:id/binding_phone_iv")
		# print(a)

		# 开本页
		self.driver.find_element_by_id("com.mg.scriptkilling:id/profile_image").click()
		time.sleep(2)
		# self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
		time.sleep(2)
		self.driver.find_element_by_id("com.mg.scriptkilling:id/id_et").send_keys("R9WN915RAVJ")
		time.sleep(2)
		self.driver.find_element_by_id("com.mg.scriptkilling:id/bind_id_tv").click()
		time.sleep(2)
		if self.is_element_exist("com.mg.scriptkilling:id/binding_phone_iv"):
			print("True")
			self.driver.find_element_by_id("com.mg.scriptkilling:id/start_game_iv").click()
		else:
			print("未绑定成功")


	def is_element_exist(self, element):
	    source = self.driver.page_source
	    if element in source:
	        return True
	    else:
	        return False


if __name__ == '__main__':
	unittest.main()