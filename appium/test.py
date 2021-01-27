#!/usr/bin/python
# coding=utf-8

import unittest
import os
from appium import webdriver
import devices
import time
import multiprocessing
import threading

def connectAdb():
	os.system('adb connect 192.168.137.144:5554')
	os.system('adb connect 192.168.137.221:5555')
	d=os.system('adb devices')
	print("设备列表")
	print(d)

class TestDM(unittest.TestCase):

	def setUp(self):
		# self.driver_port = [[4723,'R9WNA1RVQYJ'],[4729,'R9WN915RAVJ']]
		self.driver_port = [[4723,'192.168.137.144:5554'],[4729,'192.168.137.221:5555']]
		self.driver_list=[]
		for i in range(2):
			desired_caps = {}
			desired_caps['platformName'] = 'Android'
			desired_caps['deviceName'] = 'Android Pad'
			desired_caps['udid'] = self.driver_port[i][1]
			desired_caps['appPackage'] = 'com.mg.scriptkilling'
			desired_caps['appActivity'] = 'com.mg.scriptkilling.ui.login.EnterRoomActivity'
			desired_caps['unicodeKeyboard'] = True #使用unicode输入法
			desired_caps['resetKeyboard'] = True  #重置输入法到初始状态
			desired_caps['noReset'] = True  #启动app时不要清除app里的原有的数据
			print(desired_caps)
			self.driver = webdriver.Remote('http://localhost:{0}/wd/hub'.format(self.driver_port[i][0]), desired_caps)
			print(self.driver)
			self.driver.implicitly_wait(10)
			self.driver_list.append(self.driver)
		print("打印")
		print(self.driver_list)
		print(len(self.driver_list))
		print("start case test")

	def test_case1(self):
		print("dm开本")
		# 1+1演示模式
		time.sleep(3)
		# self.driver_list[0].close_app()
		# self.driver_list[0].launch_app()
		# time.sleep(3)
		# self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button").click()
		print("ok")
		time.sleep(2)

		# 首页
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/input_game_coupons_et").send_keys("18674831947")
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/activation_tv").click()
		print("enter")
		time.sleep(3)
		# self.driver.find_element_by_id("com.mg.scriptkilling:id/script_rv")[].find_element_by_id("com.mg.scriptkilling:id/script_poster_iv").click()

		# 演示剧本选择列表页
		self.driver_list[0].find_elements_by_android_uiautomator("new UiSelector().text(\"Double k\")")[0].click()
		time.sleep(2)

		if self.is_element_exist("com.mg.scriptkilling:id/binding_phone_iv", self.driver_list[0]):
			print("True")
		else:
			print("False")
		# a = self.driver.find_element_by_id("com.mg.scriptkilling:id/binding_phone_iv")
		# print(a)

		# 开本页
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/profile_image").click()
		time.sleep(2)
		# self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/id_et").send_keys("R9WN915RAVJ")
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bind_id_tv").click()
		time.sleep(2)
		if self.is_element_exist("com.mg.scriptkilling:id/binding_phone_iv", self.driver_list[0]):
			print("True")
			self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/start_game_iv").click()
		else:
			print("未绑定成功")
		time.sleep(10)

		print("玩家选择角色")
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/item").click()
		if self.is_element_exist("com.mg.scriptkilling:id/play_head", self.driver_list[1]):
			self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		else:
			print("未选择角色")
		time.sleep(5)

		print("dm下一步-自我介绍")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/menu_tv").click() #目录
		time.sleep(2)
		self.driver_list[1].find_elements_by_android_uiautomator("new UiSelector().text(\"剧本简介\")")[0].click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/x").click()
		time.sleep(2)
		a1 = self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/current_step_tv").get_attribute("text")
		time.sleep(2)
		if a1 == "自我介绍":
			print(a1)
		else:
			print("阶段文案不对")
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/bt_next_step")
		time.sleep(2)

		print("dm下一步-第一轮圆桌")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/x").click()
		time.sleep(2)
		a2 = self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/current_step_tv").get_attribute("text")
		time.sleep(2)
		if a2 == "第一轮圆桌":
			print(a2)
		else:
			print("阶段文案不对")
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/bt_next_step")
		time.sleep(2)

		print("dm下一步-第一轮搜证")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/x").click()
		time.sleep(2)
		self.driver_list[1].find_elements_by_android_uiautomator("new UiSelector().text(\"阎摩罗的房间\")")[0].click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/item").click()
		time.sleep(2)
		# self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/finish_explore_view").click()
		# time.sleep(2)
		a5 = self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/tv_content").get_attribute("text")
		time.sleep(2)
		if a5 == "阎摩罗的房间1":
			print(a5)
		else:
			print("没有这个线索")
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/collection_clues_tv").click()
		time.sleep(2)
		a3 = self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/collection_clues_tv").get_attribute("text")
		time.sleep(2)
		if a3 == "取消收藏":
			print("收藏成功")
		else:
			print("收藏失败")
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/x").click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/close").click()
		time.sleep(2)
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/finish_explore_view").click()
		time.sleep(2)

		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/script_play_info_iv").click()
		time.sleep(2)	
		a4 = self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/content").get_attribute("text")
		time.sleep(2)
		if a4 == "阎摩罗的房间1":
			print("我的线索展示正确")
		else:
			print("我的线索没展示")	
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/my_clue_collect_tv").click()
		a4 = self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/content").get_attribute("text")
		time.sleep(2)
		if a4 == "阎摩罗的房间1":
			print("我收藏的线索展示正确")
		else:
			print("我收藏的线索没展示")
		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/x").click()
		time.sleep(2)

		print("dm下一步-第二轮圆桌")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		print("dm下一步-第二轮搜证")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		print("dm下一步-第三轮圆桌")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		print("dm下一步-第三轮搜证")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		print("dm下一步-第四轮圆桌")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		print("dm下一步-指凶阶段")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/x").click()
		time.sleep(2)

		for i in range(1, 7):
			print(i)
			self.driver_list[1].find_element_by_xpath("//*[@resource-id='com.mg.scriptkilling:id/player_recyclerView']/android.view.ViewGroup[{0}]".format(i)).click()
			time.sleep(2)
			self.driver_list[1].find_element_by_xpath("//*[@resource-id='com.mg.scriptkilling:id/player_vote_rv']/android.view.ViewGroup[2]").click()
			time.sleep(2)
			self.driver_list[1].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
			time.sleep(2)

		print("dm下一步-揭晓答案")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)

		print("dm下一步-结案")
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/bt_next_step").click()
		time.sleep(2)
		self.driver_list[0].find_element_by_id("com.mg.scriptkilling:id/sure_tv").click()
		time.sleep(2)
	
	def tearDown(self):
		self.driver.quit()
		print("Finish")

	def is_element_exist(self, element, driver):
	    source = self.driver.page_source
	    if element in source:
	        return True
	    else:
	        return False


if __name__ == '__main__':
	connectAdb()
	unittest.main()