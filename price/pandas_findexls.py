# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 14:20
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : pandas_findexls.py
# @Software: PyCharm



import numpy as np
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x) # 禁用科学计数法
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


find1=pd.read_excel("数据.xlsx", sheet_name='总装')
find2=pd.read_excel("数据.xlsx", sheet_name='日计划量')
find1[find1['班组'] == '张一'][['姓名', '消费额']]
print(find1)