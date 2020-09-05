#!usr/bin/python
#coding=utf-8

import random
import MySQLdb

def random_str():
	seed_str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890'
	# seed_str = '1'
	res=''
	for x in range(16):
		res=res+random.choice(seed_str)
	return res

def remove_str(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]==l[j]:
				l[i]=-1
	x=0
	while x<len(l):
		if l[x]==-1:
			l.remove(l[x])
			x-=1
		else:
			x+=1
	return l

def main():
	res_list=[]
	db = MySQLdb.connect("127.0.0.1", "root", "", "test", charset='utf8' )
	print '连接数据库成功'
	conn = db.cursor()
	for x in range(5):		
		res_list.append(random_str())		
	remove_str(res_list)
	print res_list
	for i in res_list:
		print i
		coupon_sql = "insert into Coupons (coupon) values (%s)"
		param = [i]
		conn.execute(coupon_sql,param)
	db.commit()
	print '插入数据成功'
	conn.close()
	db.close()

if __name__ == '__main__':
	main()