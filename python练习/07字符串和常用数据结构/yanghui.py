#!/usr/bin/python

def main():
    num = int(input('Number of rows: '))
    yh=[[]]*num
    for i in range(len(yh)):
        yh[i]=[None]*(i+1)
        for j in range(len(yh[i])):
            if j==0 or j==i:
                yh[i][j]=1
            else:
                yh[i][j]=yh[i-1][j-1]+yh[i-1][j]
            print yh[i][j],
        print 

if __name__ == '__main__':
    main()