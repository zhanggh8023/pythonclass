# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 14:11
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class4_unrate.py
# @Software: PyCharm


import pandas as pd

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

# unrate = pd.read_csv('unrate1.csv')
# unrate['DATA'] = pd.to_datetime(unrate['DATA'])
# print(unrate.head(12))
print('=======================================================')
import matplotlib.pyplot as plt
# plt.plot()
# plt.show()
first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends,1948')
# plt.plot(first_twelve['DATA'],first_twelve['UNEMPLOYMENTRATE'])
# plt.xticks(rotation=45)
plt.show()
print('=======================================================')


fig =plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,4)
plt.show()
print('=======================================================')

import numpy as np
# fig =plt.figure()
fig=plt.figure(figsize=(3,6))
ax4=fig.add_subplot(2,1,1)
ax5=fig.add_subplot(2,1,2)

ax4.plot(np.random.randint(1,5,5),np.arange(5))
ax5.plot(np.arange(10)*3,np.arange(10))
plt.show()
print('=======================================================')

#两条线
unrate['MONTH'] = unrate['DATE'].dt.month
unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))

plt.plot(unrate[0:12]['MONTH'],unrate[0:12]['VALUE'],c='red')
plt.plot(unrate[12:24]['MONTH'],unrate[12:24]['VALUE'],c='blue')

plt.show()

print('=======================================================')
fig1 = plt.figure(figsize=(10,6))
colors=['red','blue','green','orange','black']
for i in range(5):
    start_index=i*12
    end_index=(i+1)*12
    subset=unrate[start_index:end_index]
    label=str(1948+i)
    plt.plot(subset['MONTH'],subset['VALUE'],c=colors[i],label=label)

plt.legend(loc='upper left')#小窗自动最合适的地方
# 'best'            0
# 'upper right'     1
# 'upper left'      2
# 'lower left'      3
# 'lower right'     4
# 'right'           5
# 'center left'     6
# 'center right'    7
# 'lower center'    8
# 'upper center'    9
# 'center'          10
#print(help(plt.legend))
plt.xlabel('Month')
plt.ylabel('Unemployment Rate, Percent')
plt.title('Monthly Unemployment Trends, 1948-1952')
plt.show()
















































