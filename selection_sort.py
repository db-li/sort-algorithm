#-*- coding:utf-8 -*-
"""
@Time: 2018-07-08
@Author: dbli
"""

def selectionsort(ary, begin, end):
    if begin==end:
        return ary
    for i in range(begin+1,len(ary)):
        if ary[i] < ary[begin]:
            temp = ary[i]
            ary[i] = ary[begin]
            ary[begin] = temp
    selectionsort(ary, begin+1, end)
    return ary

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = selectionsort(num_list,0, len(num_list)-1)
    print(new_list)