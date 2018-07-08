#-*- coding:utf-8 -*-
"""
@Time: 2018-07-08
@Author: dbli
"""

def mergearray(left, right):
    temp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1

    while i < len(left):
        temp.append(left[i])
        i +=1
    while j < len(right):
        temp.append(right[j])
        j +=1

    return temp

def mergesort(ary):
    if len(ary) <=1:
        return ary
    mid = int((end+1)/2)
    left = mergesort(a[begin:mid])
    right = mergesort(a[mid+1:end])

    return mergearray(left, right)

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = mergesort(num_list,0, len(num_list)-1)
    print(new_list)