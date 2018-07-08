#-*- coding:utf-8 -*-
"""
@Time: 2018-06-09
@Author: dbli
"""
'''
冒泡排序是一个稳定排序，时间复杂度最高
'''
def bubblesort(ary):
    for i in range(len(ary)-1):
        flag = 0
        for j in range(len(ary)-1):
            if ary[j] > ary[j+1]:
                temp = ary[j]
                ary[j] = ary[j+1]
                ary[j+1] = temp
                flag =1
        if flag == 0:
            break;
    return ary

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = bubblesort(num_list)
    print(new_list)