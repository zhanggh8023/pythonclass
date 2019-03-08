# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 21:01
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 抢红包.py
# @Software: PyCharm

import os
import sys
import subprocess
import time
import math
from PIL import Image
import random

# screenshot_way =2
#
# def pull_screenshot():
#     global screenshot_way
#     if screenshot_way==2 or screenshot_way==1:
#         process=subprocess.Popen('adb shell screencap -p',shell=True,stdout=subprocess)
#         screenshot =process.stdout.read()
#         if screenshot_way==2:
#             binary_screenshot=screenshot.replace(b'\r\n',b'\n')
#         else:
#             binary_screenshot=screenshot.replace(b'\r\r\n',b'\n')
#         f=open('autojump.png','wb')
#         f.write(binary_screenshot)
#         f.close()
#     elif screenshot_way==0:
#         os.system('adb shell screencap -p /sdcard/autojump.png')
#         os.system('adb pull /sdcard/autojump.png .')
#
#
# def click(x,y):
#     cmd='adb shell input tap {x1} {y1}'.format(
#         x1=x,
#         y1=y
#     )
#     os.system(cmd)
#     os.system('adb shell input tap 540 1200')
#     time.sleep(1)
#     os.system('adb shell input keyevent 4')
#
# def find_piece_and_board(im):
#     piece_x=169
#     piece_x_m=260
#     piece_x_r=800
#     piece_y_plus=12
#     piece_x_max=1080
#     piece_y_max=1920
#     im_pixel=im.load()
#     for i in range(200,1800,piece_y_plus):
#         pix_r=im_pixel[piece_x,i]
#         if pix_r[0]==250 and pix_r[1]==157 and pix_r[2]==59:
#             pix_r_h=im_pixel[piece_x,i+piece_y_plus]
#             if pix_r_h[0]==250 and pix_r_h[1]==157 and pix_r_h[2]==59:
#                 pix_r_r=im_pixel[piece_x_r,i]
#                 pix_r_m=im_pixel[piece_x,i]
#                 if pix_r_r[0]==250 and pix_r_r[1]==157 and pix_r_r[2]==59 and pix_r_m[0]==250 and pix_r_m[1]==157 and pix_r_m[2]==59:
#                     print('found redbag:',piece_x_m,i)
#                     click(piece_x_m,i)
#
#
# def main():
#     while True:
#         pull_screenshot()
#         im=Image.open('./autojump.png')
#         find_piece_and_board(im)
#         os.system('adb shell input swipe 1000 1200 1000 300')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#         main()
#




def main():
    while True:
        i=0
        # os.system('adb shell input swipe 1000 1600 1000 300')
        # print(os.system('adb shell input tap 500 1800'),'抢红包中。。。')
        print(os.system('adb shell input tap 540 1100'),i==1)
        # print(os.system('adb  root'))
        # print(os.system('adb shell 'sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"''))
        if i==1:
            os.system('adb shell input keyevent 4')
            i=0




if __name__ == '__main__':
    main()

