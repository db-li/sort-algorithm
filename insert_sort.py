#-*- coding:utf-8 -*-
"""
@Time: 2018-06-09
@Author: dbli
"""
'''
插入排序是一个稳定的排序，时间复杂度为n^2~n
'''
import numpy as np

def insertsort(ary):
    for i in range(1,len(ary)):
        j = i-1
        temp = ary[i]
        while(temp < ary[j] and j>=0):
            ary[j+1] = ary[j]# 如果发生变化，则需要将元素后移
            j-=1
        ary[j+1] = temp
    return ary

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = insertsort(num_list)
    print(new_list)
