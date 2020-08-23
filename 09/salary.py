#!/usr/bin/python
#coding=utf-8

"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod

class Employee(object):
	__metaclass__=ABCMeta
	"""docstring for Employee"""
	def __init__(self, name):
		super(Employee, self).__init__()
		self.name = name

	@abstractmethod
	def salary(self):
		"""工资"""
		pass

class Manager(Employee):
	"""docstring for ClassName"""
	def __init__(self,name):
		super(Manager, self).__init__(name)

	def salary(self):
		salary=15000
		print '%s的月薪为%.2f元'%(self.name,salary)

class Programmer(Employee):
	"""docstring for Programmer"""
	def __init__(self, name, duration=0):
		super(Programmer, self).__init__(name)
		self.duration = duration

	def salary(self):
		salary=150*self.duration
		print '%s的月薪为%.2f元'%(self.name,salary)


class Salesman(Employee):
	"""docstring for ClassName"""
	def __init__(self, name, sale=0):
		super(Salesman, self).__init__(name)
		self.sale = sale

	def salary(self):
		salary=1200+self.sale*0.05
		print '%s的月薪为%.2f元'%(self.name,salary)
		

def main():
	employees=[Manager('老王'),Programmer('小章',288),Salesman('小丽',502012.19)]
	for employee in employees:
		employee.salary()

if __name__ == '__main__':
	main()
