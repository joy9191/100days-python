#!/usr/bin/python
#coding=utf-8

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = '565760450@qq.com'
    receivers = ['jiuyi@mgtv.com','zhigoo.wang@gmail.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('周泥煤', 'utf-8')
    message['To'] = Header('王大锤', 'utf-8')
    message['Subject'] = Header('Python发送邮件测试', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'xzbdewappnvwbbca')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

def imagefile():
    sender = '565760450@qq.com'
    receivers = 'jiuyi@mgtv.com;zhigoo.wang@gmail.com'
    message = MIMEMultipart()

    # message['From'] = Header('周泥煤', 'utf-8')
    # message['To'] = Header('王大锤', 'utf-8')
    message['From'] = sender
    message['To'] = receivers
    message['Subject'] = Header('Python发送邮件测试', 'utf-8')

    with open('/Users/zhoujiuyi/Desktop/20200820.jpeg','rb') as fp:
        msgImage = MIMEImage(fp.read())
    msgImage.add_header('Content-ID','imgid') #为图片对象拓展标题字段和值
    message.attach(msgImage)

    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'xzbdewappnvwbbca')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    imagefile()