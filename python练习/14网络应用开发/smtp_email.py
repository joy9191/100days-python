#!/usr/bin/python
#coding=utf-8

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def textfiles():
	# 发送纯文本邮件
    sender = '565760450@qq.com'
    receivers = ['jiuyi@mgtv.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('周泥煤', 'utf-8')
    message['To'] = Header('王大锤', 'utf-8')
    message['Subject'] = Header('Python发送邮件测试', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'xzbdewappnvwbbca')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

def imagefiles():
	# 发送带附件的邮件
    sender = '565760450@qq.com'
    receivers = ['jiuyi@mgtv.com','2298058405@qq.com']
    message = MIMEMultipart('mixed')

    # message['From'] = Header('周泥煤', 'utf-8')
    # message['To'] = Header('王大锤', 'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = 'Python发送带附件的邮件测试'

    print(message)

    # with open('/Users/zhoujiuyi/Desktop/20200820.jpeg','rb') as fp:
    with open('C:/Users/KLYG/Desktop/12590.jpg','rb') as fp:	
        msgImage = MIMEImage(fp.read())
    msgImage.add_header('Content-ID','imgid') #为图片对象拓展标题字段和值
    message.attach(msgImage)

    text = "以上为自动发送邮件\n有任何问题请联系我"
    text_plain = MIMEText(text,'plain', 'utf-8')
    message.attach(text_plain)

    try:
    	smtper = SMTP('smtp.qq.com')
    	# 发送方邮箱授权码
    	smtper.login(sender, 'xzbdewappnvwbbca')
    	smtper.sendmail(sender, message['To'].split(','), message.as_string())
    	print('邮件发送完成!')
    except smtplib.SMTPException as e:
    	print('ERROR:无法发送邮件.Case:%s'%e)

def htmlfiles():
	sender = '565760450@qq.com'
	receivers = ['jiuyi@mgtv.com','2298058405@qq.com']
	message = MIMEMultipart('mixed')

	message['From'] = sender
	message['To'] = ','.join(receivers)
	message['Subject'] = 'Python发送HTML邮件测试'
	# with open('C:/Users/KLYG/Desktop/12590.jpg','rb') as fp:
	# 	msgImage = MIMEImage(fp.read())

	fp=open('C:/Users/KLYG/Desktop/12590.jpg','rb')
	msgImage=MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID','<img1>')
	message.attach(msgImage)

	content= '<h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '<img src="cid:img1" alt="书房" />'

	htm=MIMEText(content, 'html', 'utf-8')
	message.attach(htm)

	try:
		smtper = SMTP('smtp.qq.com')
		# 发送方邮箱授权码
		smtper.login(sender, 'xzbdewappnvwbbca')
		smtper.sendmail(sender, message['To'].split(','), message.as_string())
		print('邮件发送完成!')
	except smtplib.SMTPException as e:
		print('ERROR:无法发送邮件.Case:%s'%e)


if __name__ == '__main__':
    textfiles()