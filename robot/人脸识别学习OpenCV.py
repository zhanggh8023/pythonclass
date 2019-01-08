# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 16:37
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 121.py
# @Software: PyCharm


#取图片
# import cv2

# print(cv2.__version__)
# filepath = "D:\git_home\\faceai\\res\chinese.png"
# img = cv2.imread(filepath)
# cv2.namedWindow('Image')
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#图片文字识别
# from PIL import Image
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#
# path = "text-img.png"
#
# text = pytesseract.pytesseract.image_to_string(Image.open(path), lang='chi_sim')
# print(text)

#图片转灰色
import cv2

# filepath = "D:\git_home\\faceai\\faceai\img\\xingye-1.png"
# img = cv2.imread(filepath)
# # 转换灰色
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # 显示图像
# cv2.imshow("Image", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 图片上画矩形
# filepath = "D:\git_home\\faceai\\faceai\img\\xingye-1.png"
# img = cv2.imread(filepath)  # 读取图片
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
# x = y = 10  # 坐标
# w = 100  # 矩形大小（宽、高）
# color = (0, 0, 255)  # 定义绘制颜色
# cv2.rectangle(img, (x, y), (x + w, y + w), color, 1)  # 绘制矩形
# cv2.imshow("Image", img)  # 显示图像
# cv2.waitKey(0)
# cv2.destroyAllWindows()  # 释放所有的窗体资源


#使用训练分类器查找人脸

filepath = "D:\git_home\\faceai\\faceai\img\\xingye-1.png"
img = cv2.imread(filepath)  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色

# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    "D:\Python\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
)
color = (0, 255, 0)  # 定义绘制颜色
# 调用识别人脸
faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)

cv2.imshow("image", img)  # 显示图像
c = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()