# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 18:11
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class4_unrate2.py
# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt

women_degres = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
major_cats=['Biology','Computer Science','Engineering','Math and Statistics']
# fig= plt.figure(figsize=(18,3))

cb_dark_blue=(0/255,107/255,164/255)
cb_orange=(255/255,128/255,14/255)

fig = plt.figure(figsize=(12,12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    # the color for each line is assigned here.
    ax.plot(women_degres['Year'],women_degres[major_cats[sp]],c=cb_dark_blue,label='Women')
    ax.plot(women_degres['Year'],100-women_degres[major_cats[sp]],c=cb_orange,label='Men')
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    ax.set_title(major_cats[sp])
    ax.tick_params(bottom='off',top='off',left='off',right='off')

plt.legend(loc='upper right')
plt.show()

























