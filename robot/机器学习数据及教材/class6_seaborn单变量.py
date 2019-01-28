# -*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:49
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class6_seaborn单变量.py
# @Software: PyCharm


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats, integrate

sns.set(color_codes=True)
np.random.seed(sum(map(ord,'disrtibutions')))

x= np.random.normal(size=100)
sns.distplot(x,kde=False)
plt.show()

sns.distplot(x,bins=20,kde=False)
plt.show()

# 数据分布
x = np.random.gamma(6,size=100)
sns.distplot(x,kde=False,fit=stats.gamma)
plt.show()


#根据均值和协方差生成数据
mean,cov=[0,2],[(1,5),(5,1)]
data = np.random.multivariate_normal(mean,cov,200)
df =pd.DataFrame(data,columns=['x','y'])
print(df)


#观测两个变量之间的分布关系最好用散点图
sns.jointplot(x='x',y='y',data=df)
plt.show()


x, y = np.random.multivariate_normal(mean,cov,1000).T
with sns.axes_style('white'):
    sns.jointplot(x=x,y=y,kind='hex',color='k')
plt.show()

iris=sns.load_dataset('iris')
sns.palplot(iris)











