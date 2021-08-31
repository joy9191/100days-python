#!/usr/bin/python
#coding=utf-8
import pymysql

def addDept():
	# 添加部门数据表
	no = int(input('编号: '))
	name = raw_input('名字: ')
	loc = raw_input('所在地: ')
	con = pymysql.connect(host='localhost', port=3306,
                          database='cnbeta', charset='utf8',
                          user='root', password='joy890621',
                          autocommit =True)
	try:
		# 使用with as语句操作上下文管理器，作用是确保数据库使用完后会关闭连接
    	# 使用with as无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件
		with con.cursor() as cursor:
			result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (no, name, loc)
            )
        	print(result)
        	if result==1:
        		print('添加成功!')
        # 4. 操作成功提交事务
        	# con.commit()
        finally:
        	con.close()

def delDept():
	no = int(input('要删除的部门编号: '))
	con = pymysql.connect(host='localhost', port=3306,
                          database='cnbeta', charset='utf8',
                          user='root', password='joy890621',
                          autocommit =True)
	try:
		with con.cursor() as cursor:
			result = cursor.execute(
				'delete from tb_dept where dno=%s',no
				)
			print(result)
			if result==1:
				print('没有该数据，删除成功！')
	finally:
		con.close()

if __name__ == '__main__':
	addDept()
	delDept()