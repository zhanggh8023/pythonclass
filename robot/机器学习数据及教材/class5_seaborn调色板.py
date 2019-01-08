# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 11:04
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class5_seaborn调色板.py
# @Software: PyCharm

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(6,6)})
'''调色板
颜色很重要
color_palette()能传入任何Matplotlib所支持的颜色
color_palette()不写参数则默认颜色
set_palette()设置所有图的颜色'''

# current_palette=sns.color_palette()
# # 默认的十个颜色循环主题
# sns.palplot(current_palette)
# plt.show()
# # 可使用hls的颜色空间，这是个RGB值的一个简单转换，设置8份
# sns.palplot(sns.color_palette('hls',8))
# plt.show()
#
# data=np.random.normal(size=(20,8))+np.array(8)/2
# sns.boxplot(data=data,palette=sns.color_palette('hls',8))#指定颜色域进行上色
# plt.show()
#
# # hls_palette()函数来控制颜色的亮度和饱和度：l-亮度lightness；s-饱和度saturation
# sns.palplot(sns.hls_palette(8,l=7,s=9))# 选择亮度饱和度
#
# sns.palplot(sns.color_palette('Paired',10))# 分对来体现同一国家同色深浅
#

# 使用xkcd颜色来命名颜色：包含了一套众包努力的正对随机RGB色的命名，产生954个可随时通过xdcd_rgb
# 字典中调用的命名颜色。
plt.plot([0,1],[0,1],sns.xkcd_rgb['pale red'],lw=3)
plt.plot([0,1],[0,2],sns.xkcd_rgb['medium green'],lw=3)
plt.plot([0,1],[0,3],sns.xkcd_rgb['denim blue'],lw=3)
plt.show()

#连续色板：色彩岁数据变化，比如数据越来越重要，颜色就越来越深
# sns.palplot(sns.color_palette('Blues'))#由浅到深
# plt.show()
#
# sns.palplot(sns.color_palette('Blues_r'))#由深到浅
# plt.show()
#
# sns.palplot(sns.color_palette('cubehelix',8))#线性变换的，色弱
# plt.show()
#
# sns.palplot(sns.cubehelix_palette(8,start=5,rot=75))#指定区间变化
# plt.show()

#light_palette()和 dark_palette()调用定制连续色板
# sns.palplot(sns.dark_palette('green'))
# sns.palplot(sns.light_palette('blue',reverse=True))#翻转颜色深浅
# plt.show()

#渐变色
x,y =np.random.multivariate_normal([0,0],[[1,-.5],[-.5,1]],size=300).T
pal=sns.dark_palette('green',as_cmap=True)
sns.kdeplot(x,y,cmap=pal)
plt.show()













