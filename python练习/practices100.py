# -*- coding: utf-8 -*-
def three_figure():
	n=0
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				if (i!=j and j!=k and k!=i):
					n=n+1
					print(100*i+10*j+k)	
	print(n)

def bonus():
	profit = int(input("净利润："))
	arr = [1000000,600000,400000,200000,100000,0]
	rate = [0.01,0.015,0.03,0.05,0.075,0.1]
	b = 0
	for i in range(0,6):
		if profit>arr[i]:
			b += (profit-arr[i])*rate[i]
			print((profit-arr[i])*rate[i])
			profit = arr[i]
	return b

def nums():
	for i in range(2,85):
	    if 168 % i == 0:
	        j = 168 / i;
	        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
	            m = (i + j) / 2
	            n = (i - j) / 2
	            x = n * n - 100
	            print(x)


def days():
	year = int(input("year:\n"))
	month = int(input("mouth:\n"))
	day = int(input("day:\n"))

	
	months = (0,31,59,90,120,151,181,212,243,273,304,334)
	if 0<month<=12:
		day1=months[month-1]
	else:
		print("data error")

	leap = 0
	if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):
		leap = 1
	if (leap == 1) and (month > 2):
		day1 +=1
	
	print(day1+day)



if __name__ == '__main__':
	# three_figure()
	# print(bonus())
	# nums()
	days()
