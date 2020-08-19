#!/usr/bin/python
#coding=utf-8

from time import sleep
import datetime
import os

class Clock(object):
	"""docstring for Clock"""
	def __init__(self, hour=0, minute=0, second=0):
		super(Clock, self).__init__()
		self._hour = hour
		self._minute = minute
		self._second = second

	def run(self):
		self._second+=1
		if self._second==60:
			self._minute+=1
			self._second=0
			if self._minute==60:
				self._hour+=1
				self._minute=0
				if self._hour==24:
					self._hour=0

	def show(self):
		return '现在时间是：%02d:%02d:%02d'%(self._hour,self._minute,self._second)


def main():
	nowTime=datetime.datetime.now()
	nowH=nowTime.strftime('%H')
	nowM=nowTime.strftime('%M')
	nowS=nowTime.strftime('%S')
	now=Clock(int(nowH),int(nowM),int(nowS))
	while True:
		os.system('clear')
		print now.show()
		sleep(1)
		now.run()



if __name__ == '__main__':
    main()