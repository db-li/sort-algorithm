#-*- coding:utf-8 -*-
"""
@Time: 2018-07-08
@Author: dbli
"""

def shellsort(ary):

    gap = len(ary)
    while gap > 0:
        gap = int(gap / 2)
        for i in range(gap, len(ary)):
            while i >= gap and ary[i-gap] > ary[i]:
                temp = ary[i-gap]
                ary[i-gap] = ary[i]
                ary[i] = temp
                i -= gap
    return ary

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = shellsort(num_list)
    print(new_list)