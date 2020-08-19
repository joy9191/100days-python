#!/usr/bin/python
#coding=utf-8
from math import sqrt

class Point(object):
	"""docstring for Point"""
	def __init__(self, x=0, y=0):
		super(Point, self).__init__()
		# x横坐标，y纵坐标
		self.x = x
		self.y = y

	def move(self,tx,ty):
		self.x+=tx
		self.y+=ty

	def distance(self,other):
		dx=self.x-other.x
		dy=self.y-other.y
		return sqrt(dx ** 2 + dy ** 2)

	def __str__(self):
		return '(%s,%s)'%(str(self.x),str(self.y))
		
def main():
	point1=Point(3,6)
	point2=Point()
	print point1
	print point2
	point1.move(-1,5)
	print point1
	print(point1.distance(point2))

if __name__ == '__main__':
	main()