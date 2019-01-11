# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 0:19
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 冒泡排序.py
# @Software: PyCharm
# 冒泡排序算法


class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def bubble_sort_simple(self):
        """
        最简单的交换排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if lis[i] > lis[j]:
                    self.swap(i, j)

    def bubble_sort(self):
        """
        冒泡排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            j = length-2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                j -= 1

    def bubble_sort_advance(self):
        """
        冒泡排序改进算法，时间复杂度O(n^2)
        设置flag，当一轮比较中未发生交换动作，则说明后面的元素其实已经有序排列了。
        对于比较规整的元素集合，可提高一定的排序效率。
        """
        lis = self.r
        length = len(self.r)
        flag = True
        i = 0
        while i < length and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis[j + 1]:
                    self.swap(j, j + 1)
                    flag = True
                j -= 1
            i += 1

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret

if __name__ == '__main__':
    sqlist = SQList([4,1,7,3,8,5,9,2,6])
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.bubble_sort_advance()
    print(sqlist)# 冒泡排序算法


class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        """定义一个交换元素的方法，方便后面调用。"""
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def bubble_sort_simple(self):
        """
        最简单的交换排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if lis[i] > lis[j]:
                    self.swap(i, j)

    def bubble_sort(self):
        """
        冒泡排序，时间复杂度O(n^2)
        """
        lis = self.r
        length = len(self.r)
        for i in range(length):
            j = length-2
            while j >= i:
                if lis[j] > lis[j+1]:
                    self.swap(j, j+1)
                j -= 1

    def bubble_sort_advance(self):
        """
        冒泡排序改进算法，时间复杂度O(n^2)
        设置flag，当一轮比较中未发生交换动作，则说明后面的元素其实已经有序排列了。
        对于比较规整的元素集合，可提高一定的排序效率。
        """
        lis = self.r
        length = len(self.r)
        flag = True
        i = 0
        while i < length and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis[j + 1]:
                    self.swap(j, j + 1)
                    flag = True
                j -= 1
            i += 1

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret



import random


def bubblesort(target):
    length = len(target)
    while length > 0:
        length -= 1
        cur = 0
        while cur < length: #拿到当前元素
            if target[cur] < target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
if __name__ == '__main__':
    a = [random.randint(1,1000) for i in range(100)]
    print (bubblesort(a))
    print(sorted(a))
    a.sort()
    print(a)


    sqlist = SQList([4,1,7,3,8,5,9,2,6])
    # sqlist.bubble_sort_simple()
    # sqlist.bubble_sort()
    sqlist.bubble_sort_advance()
    print(sqlist)
