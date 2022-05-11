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
			print(b)
	return b


if __name__ == '__main__':
	# three_figure()
	print(bonus())
