#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import string

def coupon():
	couponNum = ''
	for x in range(0,10):
		couponNum += str(random.choice(string.ascii_letters + string.digits))
	return couponNum

def couponCode():
	couponIndex=60000
	for i in range(10):
		couponIndex += 1
		couponNum = coupon()
		couponNum = couponNum[:4]+ str(couponIndex) +couponNum[5:]
		print(couponNum)


if __name__ == '__main__':
	couponCode()