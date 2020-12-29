#!/usr/bin/python
# coding=utf-8

import unittest
from appium import webdriver
import time

class ConcurrentExecution:
      """
      多进程并发安装本地apk
      """
          def __init__(self):
     　　　 　　self.driver_port = [[4723,"127.0.0.1:21503"],[4729,"127.0.0.1:21513"]]

    def android_driver(self,i):
         driver_list = []
         capabilities = {
                "platformName"  : "Android",
                "udid"                   : self.driver_port[i][1],
                "deviceName"      : self.driver_port[i][1],
                "app"                    : "E:\\appiumautocode\\xxxoooox.apk",
                "noReset"             : "True"
                 }
         driver = webdriver.Remote("http://127.0.0.1:{0}/wd/hub".format(self.driver_port[i][0]),capabilities)
         driver_list.append(driver)
       　return driver_list