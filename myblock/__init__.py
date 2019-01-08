# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 13:25
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : __init__.py.py
# @Software: PyCharm

from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
    a=hash(5 * 21)
print(f'The solution is y = {y}',a)
