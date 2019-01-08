# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 13:29
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class2.py
# @Software: PyCharm

import numpy

#会查方法使用  help
# test=open('world_alcohol.txt','w')
# w=test.write('根据模型的分类或者模型的状态进行筛选模型，根据所选择相对应类目或者状态下的模型，状态和类目支持同时选择')
# test.close()
# world_alcohol=numpy.genfromtxt('world_alcohol.txt',delimiter=',',dtype=str)
# print(type(world_alcohol))
# print(world_alcohol)
# print(help(numpy.genfromtxt))


#矩阵使用
vector=numpy.array([5,10,15,20])
matrix=numpy.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix)
print(vector)

#属性
vector=numpy.array([5,10,15,20])
print(vector.shape)
matrix=numpy.array([[5,10,15],[20,25,30],[35,40,45],[45,50,55]])
print(matrix.shape)


#类型统一
numders=numpy.array([1,2,3,4,5,])
print(numders)
numpy.dtype
numders1=numpy.array([1,2,3,4,5,'6'])
print(numders1)
numpy.dtype


#数据读取
world_alcoho2=numpy.genfromtxt('world_alcohol.txt',delimiter=',',dtype=str,skip_header=0)
print(world_alcoho2)

world=world_alcoho2[1]
third_country=world[3]
print(world)
print(third_country)

#判断
vector=numpy.array([5,10,15,20,25])
print(vector == 10)

#返回值
r=(vector == 10)
print(vector[r])


#类型转换
vector=numpy.array(['1','2','3','4'])
print(vector.dtype)
print(vector)
vector=vector.astype(float)
print(vector.dtype)
print(vector)
print(vector.min())
print(vector.max())


matrix=numpy.array([[5,10,15],
                    [20,25,30],
                    [35,40,45],
                    [45,50,55]])
print(matrix.sum(axis=1))
print(matrix.sum(axis=0))


import numpy as np
print(np.arange((15)))
a=np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.size)



#零矩阵
print(np.zeros((3,4)))
print(np.ones((2,3,4),dtype=np.int32))


print(np.arange(1,30,5))#一次加五，直到小于30
print(np.arange(12).reshape(4,3))#十二个数，四行每行三数



#权证矩阵
np.random.random((2,3))
print(np.random.random((2,3)))

from numpy import pi
print(np.linspace(0,2*pi,100))


#矩阵加减乘除
a=np.array([20,30,40,50])
b=np.arange(4)
print(a)
print(b)
c=a-b
print(c)
c=c-1
print(c)
b**2
print(b**2)
print(a<35)

#乘法
A=np.array([[1,1],
            [0,1]])
B=np.array([[3,4],
            [5,6]])
print(A)
print('---------------')
print(B)
print('------------------')
print(A*B)
print('-------------------')
print(A.dot(B))
print([ A[0,0] * B[0,0] + A[0,1] * B[1,0] , A[0,0] * B[0,1] + A[0,1] * B[1,1] ] , [ A[1,0] * B[0,0] + A[1,1] * B[1,0] , A[1,0] * B[0,1] + A[1,1] * B[1,1]] )
print('----------------')
print(np.dot(A,B))

#矩阵变化
a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.ravel())

a.shape = (6,2)
print(a)
print(a.T)
































































