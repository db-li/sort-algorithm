#-*- coding:utf-8 -*-
"""
@Time: 2018-06-09
@Author: dbli
"""
'''
1、i＝1为根
2、i>1 则父结点存在，为i/2向下取整
3、2i>n则没有左孩子
   2i<＝n，左孩子为2i
4、2i＋1>n则没有右孩子
   2i＋1<＝n，右孩子为2i+1
n为结点个数   
   
      1
  2       3
4   5   6   7
   
'''
def mix_sort(head, lchild, rchild):
    temp = head
    flag = 1
    if rchild is None:
        if head < lchild:
            head = lchild
            lchild = temp
    else:
        if head <lchild or head< rchild:
            if rchild < lchild:
                head = lchild
                lchild = temp
            elif rchild > lchild:
                head = rchild
                rchild = temp

    return head, lchild, rchild



def heapsort(s, begin, end):

    if (end+1)<=1:
        return s

    lastfasernode = int((end+1)/2)
    i = lastfasernode

    while (i <= lastfasernode and i >0):
        lchild = i*2
        rchild = i*2+1
        lch =  s[lchild-1]
        if rchild > (end+1):
            rch = None
            s[i - 1], s[lchild - 1], rch = mix_sort(s[i - 1], lch, rch)
        else:
            rch = s[rchild-1]
            s[i-1],s[lchild-1],s[rchild-1] = mix_sort(s[i-1],lch,rch)
        i -=1

    temp = s[0]
    s[0] = s[end]
    s[end] = temp
    heapsort(s, begin, end-1)
    return s

if __name__=="__main__":
    num_list = [67,23,89,35,28,90,10,24]
    new_list = heapsort(num_list, 0, len(num_list)-1)
    print(new_list)
