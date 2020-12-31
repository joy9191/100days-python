#!/usr/bin/python
# coding=utf-8

import os
from appium import webdriver

class Launch():
	def __init__(self):
		self.driver_port = [[4723,'R9WNA1RVQYJ'],[4729,'R9WN915RAVJ']]

	def android_driver(self,i):
		driver_list = []
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['udid'] = self.driver_port[i][1]
		desired_caps['appPackage'] = 'com.mg.scriptkilling'
		desired_caps['appActivity'] = 'com.mg.scriptkilling.ui.login.EnterRoomActivity'
		desired_caps['unicodeKeyboard'] = True #使用unicode输入法
		desired_caps['resetKeyboard'] = True  #重置输入法到初始状态
		desired_caps['noReset'] = True  #启动app时不要清除app里的原有的数据
		driver = webdriver.Remote('http://localhost:{0}/wd/hub'.format(self.driver_port[i][0]), desired_caps)
		driver.implicitly_wait(10)
		driver_list.append(driver)
		return driver_list

	# def start_appium_server(self,j):
	# 	li_port = [4723,4729]
	# 	os.system("appium -p {0}".format(li_port[j]))

if __name__ == '__main__':
	obj=devices.Launch()
	print(obj)
	# 启动
	for j in range(2): 
		th = threading.Thread(target=obj.start_appium_server,args=(j,))
		th.start()
	# 运行
	for i in range(2): 
		t = multiprocessing.Process(target=obj.android_driver,args=(i,))
		print(t)
		t.start()