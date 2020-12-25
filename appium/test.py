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
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(10)
		print("start case test")

	def tearDown(self):
		self.driver.quit()
		print("Finish")

	def test_case1(self):
		print("case1")
		time.sleep(3)
		self.driver.close_app()
		self.driver.launch_app()
		time.sleep(3)

if __name__ == '__main__':
	unittest.main()