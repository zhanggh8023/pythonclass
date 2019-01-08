# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 8:59
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 视频检测人脸.py
# @Software: PyCharm

import cv2

# #获取摄像头
# cap = cv2.VideoCapture(0)
#
# #显示摄像头
# while (1):
#     ret, img = cap.read()
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()  # 释放摄像头
# cv2.destroyAllWindows()  # 释放窗口资源
#
# #视频的人脸识别
#
# def discern(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cap = cv2.CascadeClassifier(
#         "D:\Python\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
#     )
#     faceRects = cap.detectMultiScale(
#         gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
#     if len(faceRects):
#         for faceRect in faceRects:
#             x, y, w, h = faceRect
#             cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
#     cv2.imshow("Image", img)
#
# # 获取摄像头0表示第一个摄像头
# cap = cv2.VideoCapture(0)
# while (1):  # 逐帧显示
#     ret, img = cap.read()
#     # cv2.imshow("Image", img)
#     discern(img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()  # 释放摄像头
# cv2.destroyAllWindows()  # 释放窗口资源


# 图片识别方法封装
def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier(
        "D:\Python\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
    )
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    cv2.imshow("Image", img)


# 获取摄像头0表示第一个摄像头
cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    # cv2.imshow("Image", img)
    discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源










