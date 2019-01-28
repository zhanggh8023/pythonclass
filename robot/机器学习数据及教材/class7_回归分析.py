# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 10:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class7_回归分析.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

sns.set(color_codes=True)

np.random.seed(sum(map(ord,'regression')))

tips=sns.load_dataset('tips')
tips.head()

plt.show()








