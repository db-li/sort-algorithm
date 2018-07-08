#-*- coding:utf-8 -*-
"""
@Time: 2018-07-08
@Author: dbli
"""
'''
通过重点地方保证队列中有一个空余的位置，使换位成为可能
'''
import numpy as np


def quicksort(ary, low, hight):
    left = low
    right = hight
    if left >= right:
        return ary

    key = ary[left]

    while left < right:
        while left< right and ary[right] >= key:
            right -= 1
        ary[left] = ary[right]# 重点
        while left < right and ary[left] <= key:
            left += 1
        ary[right] = ary[left]# 重点
    ary[left] = key
    quicksort(ary, low, left-1)
    quicksort(ary, right+1, hight)
    return ary

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = quicksort(num_list,0, len(num_list)-1)
    print(new_list)