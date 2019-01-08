# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 13:59
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : sco1.py
# @Software: PyCharm


m = int(input())
n = int(input())
c = list(map(int,input().split()))
dp = [100000]*(m+1)
dp[0] = 0
for i in range(n):
    for j in range(m,c[i]-1,-1):
        dp[j]=min(dp[j],dp[j-c[i]]+1)
if dp[m]>=100000:
    print(0)
else:
    print(dp[m])
