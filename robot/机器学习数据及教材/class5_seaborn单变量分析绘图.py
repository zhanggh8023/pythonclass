# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 14:03
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class5_seaborn单变量分析绘图.py
# @Software: PyCharm


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats, integrate
sns.set(color_codes=True)
np.random.seed(sum(map(ord,'distributions')))


x =np.random.normal(size=100)
sns.distplot(x,kde=False)#直方图
plt.show()















