#!/usr/bin/python
def findMax(x):
	for i in range(len(x)-1):
		for j in range(len(x)-i-1):
			if x[j]>x[j+1]:
				x[j],x[j+1]=x[j+1],x[j]
	return x[-1],x[-2]

if __name__ == '__main__':
	print findMax([1,8,10,83,2,13])