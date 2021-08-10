#!/usr/bin/python
#coding=utf-8
import MySQLdb

def main():
	# 添加部门数据表
	no = int(input('编号: '))
	name = raw_input('名字: ')
	loc = raw_input('所在地: ')
	con = MySQLdb.connect(host='localhost', port=3306,
                          database='cnbeta', charset='utf8',
                          user='root', password='joy890621')
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
        	con.commit()
        finally:
        	con.close()

if __name__ == '__main__':
	main()