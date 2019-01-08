# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 9:03
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 33.py
# @Software: PyCharm

import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
import missingno as msno
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)


# - 数据集的大小：[10886 rows x 12 columns]
dailyData = pd.read_csv("train.csv")
# pd.set_option('display.max_rows', None) # 设置显示最大行
# pd.set_option('display.max_columns', None) # 设置显示最大列，None为显示所有列
# print(dailyData)
print(dailyData.shape)


## （三）：构造变量类型的dataframe并画图展示

# - 计算不同类型的变量个数（category，int,float,object）
dataTypeDf = pd.DataFrame(dailyData.dtypes.value_counts())
print(dataTypeDf)#dataTypeDf数据组不是很明白怎么理解
a=dataTypeDf.reset_index()
print(a)
b=a.rename(columns={"index":"variableType",0:"count"})
print(b)

# - 使用seaborn的barplot进行画图展示
fig, ax = plt.subplots()
fig.set_size_inches(12, 5)
sn.barplot(data=b,x='variableType', y='count',ax=ax)#这里还有问题未能理解报错原因,dataTypeDf数据组不是很明白怎么理解
ax.set(xlabel='variableTypeariable Type', ylabel='Count',title='Variables DataType Count')
plt.show()

