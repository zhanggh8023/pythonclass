# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 15:41
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 性别识别.py
# @Software: PyCharm



#性别识别

import cv2
from keras.models import load_model
import numpy as np
import chineseText

#img = cv2.imread("gather.png")
img = cv2.imread(".\\face_recognition\zhanggh.png")

face_classifier = cv2.CascadeClassifier(
    "D:\Python\Python36\Lib\site-packages\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml"
)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(140, 140))

gender_classifier = load_model(
    "simple_CNN.81-0.96.hdf5")
gender_labels = {0: '女', 1: '男'}
color = (255, 255, 255)

for (x, y, w, h) in faces:
    face = img[(y - 60):(y + h + 60), (x - 30):(x + w + 30)]
    face = cv2.resize(face, (48, 48))
    face = np.expand_dims(face, 0)
    face = face / 255.0
    gender_label_arg = np.argmax(gender_classifier.predict(face))
    gender = gender_labels[gender_label_arg]
    cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
    img = chineseText.cv2ImgAddText(img, gender, x + h, y, color, 30)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()