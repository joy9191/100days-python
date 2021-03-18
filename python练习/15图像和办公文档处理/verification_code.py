#!/usr/bin/python
# coding=utf-8

# import sys
# sys.path.append(r'D:\Users\KLYG\Anaconda3\Lib\site-packages')
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 如果我们想要对图片进行操作，先要获取图片对象，再调用方法
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 存储随机验证码
codes=''
# 填充文字:
for t in range(4):
	rndcode=rndChar()
	draw.text((60 * t + 10, 10), rndcode, font=font, fill=rndColor2())
	codes+=rndcode
print codes

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.show()
image.save('code.jpg', 'jpeg')