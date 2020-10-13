# python文件操作
* 读文件
使用内置函数
``f = open('E:\python\python\test.txt', 'r')``
其中r参数表示读（read）
这时如果文件不存在，则会报错
``
f=open('E:\python\python\test.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'E:\python\python\test.txt``
如果可以成功打开，可使用read()方法一次性读取文件内容，得到一个str对象

