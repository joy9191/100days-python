#!/usr/bin/python
#coding=utf-8

import sys
sys.path.append(r'D:\Users\KLYG\Anaconda3\Lib\site-packages')
from PIL import Image

image = Image.open('C:/Users/KLYG/Desktop/12590.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
for x in range(80, 310):
	for y in range(20, 360):
		image.putpixel((x, y), (128, 128, 128))
image.show()