# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 16:46
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.py
# @Software: PyCharm

# class TEST():
#     def String(self, str):
#         s_dic = {}
#         s_ls = []
#         for i in str:
#             # print(i)
#             if i not in s_dic.keys():
#                 s_dic[i] = 1
#                 s_ls.append(i)
#                 # print(s_ls,s_dic)
#             else:
#                 s_dic[i] += 1
#         for j in s_ls:
#             # print(j)
#             if s_dic[j] == 1:
#                 return j
#         else:
#             return '没有符合条件数据'
#
# if __name__ == '__main__':
#     s=TEST().String('sssfasseffeead322')
#     print(s)
# #case1='ababccddeeff'
# #case2='abaccsseef'
# #case3='sssfasseffeead322'


import random

def test(arr):
    arr_lis = []
    try:
        for ii in range(int(arr)):
            arr_lis.append(ii)
    except:
        return '请输入整数！'


    for i in range(1, len(arr_lis) - 1):
        ran = random.randint(0, i)
        value = arr_lis[ran]
        value_index = arr_lis.index(value)
        arr_lis.pop(value_index)
        arr_lis.append(value)

    print(arr_lis)

h=test(input('请输入整数：'))