# -*- coding:utf-8 -*-
#!/usr/bin/python

f=float(input('请输入华氏温度: '))
c=(f-32)*5/9
print '%.1f'%c

# 1、代码中有中文时第一行必须带有# -*- coding:utf-8 -*-
# 2、控制小数点后面的位数'%.1f'%c，或者调用round()函数，e.g.round(x,1)