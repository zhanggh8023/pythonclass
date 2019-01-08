# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 16:59
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class5_seaborn.py
# @Software: PyCharm

'''Python关于%matplotlib inline
其中最后一句%matplotlib inline比较奇怪，而且无论你是用哪个python的IDE如spyder或者pycharm,这个地方都会报错，显示是invalid syntax（无效语法）。那为什么代码里面还是会有这一句呢？原来是这样的。
%matplotlib作用

是在使用jupyter notebook 或者 jupyter qtconsole的时候，才会经常用到%matplotlib，也就是说那一份代码可能就是别人使用jupyter notebook 或者 jupyter qtconsole进行编辑的。关于jupyter notebook是什么，可以参考这个链接：[Jupyter Notebook介绍、安装及使用教程][1]
而%matplotlib具体作用是当你调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，可以直接在你的python console里面生成图像。
而我们在spyder或者pycharm实际运行代码的时候，可以直接注释掉这一句，也是可以运行成功的。如下示例：

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)

如图所示，生成了一个带坐标轴的figure对象，并且画布颜色是白色的。

想在pycharm中也实现和%matplotlib inline同样的效果，把图画出来

 plt.show()
'''
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#%matplotlib inline  #



#整体风格设置
def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

sinplot()
plt.show()

# sns.set()
# sinplot()
# plt.show()

#五种风格：darkgrid/whitegrid/dark/white/ticks/

sns.set_style('whitegrid')#设置风格
data=np.random.normal(size=(20,6))+ np.arange(6)/2
# sns.boxplot(data=data)
# plt.show()
#
# sns.set_style('ticks')
# sinplot()
# sns.despine()#去除上部线和右线
# plt.show()

# sns.violinplot(data)
# sns.despine(offset=30)#画图离轴线距离设置
# plt.show()

# sns.set_style('whitegrid')
# sns.boxplot(data=data,palette='deep')
# sns.despine(left=True)#设置保留轴隐藏
# plt.show()

with sns.axes_style('darkgrid'):#指定域画图风格
    plt.subplot(211)
    sinplot()
    # plt.show()
plt.subplot(212)
sinplot(-1)
plt.show()

sns.set()
#指定格子大小,刻度字体大小，线的粗细等
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':2.5})
plt.figure(figsize=(8,6))
sinplot()
plt.show()


































