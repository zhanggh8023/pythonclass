# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 15:01
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : reading_code.py
# @Software: PyCharm

import pytesseract
import pycapt
from PIL import Image

image = Image.open("validCodeImage.jpg")
image = image.convert("L")
threshold = 110
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = pytesseract.image_to_string(image)
print(result)

img = Image.open('validCodeImage.jpg')
img = pycapt.two_value(img, Threshold=100)
img = pycapt.dele_noise(img, N=5, Z=2)

# img = pycapt.dele_line(img,4)
# img = pycapt.dele_noise(img,N=4,Z=2)
# img = pycapt.dele_line(img,3)
# img = pycapt.dele_noise(img,N=4,Z=2)
# img = pycapt.dele_line(img,3)
# img = pycapt.dele_line(img,2)
# img = pycapt.dele_line(img,1)

img = Image.open('validCodeImage.jpg')
img_list = pycapt.cut_img_to_img_list(img,max_width=30,background=255)
for i in img_list:
    i.show()


name,img = pycapt.do_captcha(
        my_str_list=['A','B','C','D','1','2','3'],
        width=160,
        height=40,
        num_of_str=4,
        font=30,
        gray_value=255,
        font_family='msyh.ttc')

print(name)


# output： ['C', 'D', '2', 'A']
img.show()
