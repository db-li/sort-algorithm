#-*- coding:utf-8-*-

def mix_sort(head, lchild, rchild):
    temp = head
    flag = 1
    if rchild is None:
        if head >= lchild:
            flag = 0
        else:
            head = lchild
            lchild = temp
    else:
        if head >=lchild and head>= rchild:
            flag = 0
        else:
            if rchild < lchild:
                head = lchild
                lchild = temp
            elif rchild > lchild:
                head = rchild
                rchild = temp
            flag = 1
    return head, lchild, rchild, flag

def creat_heapsort(s):
    lastnode = int(len(s)/2)
    while True:
        i = lastnode
        while (i < lastnode+1 and i >0):
            lchild = i*2
            rchild = i*2+1
            lch =  s[lchild-1]
            if rchild > len(s):
                rch = None
                s[i - 1], s[lchild - 1], rch, flag = mix_sort(s[i - 1], lch, rch)
            else:
                rch = s[rchild-1]
                s[i-1],s[lchild-1],s[rchild-1],flag = mix_sort(s[i-1],lch,rch)
            i -=1
        if flag==0:
            break
    temp = s[0]
    s[0] = s[-1]
    s[-1] = temp
    return s

def heapsort(ary):
    new_list = []
    new_list = creat_heapsort(ary)
    print(new_list)
    heapsort(new_list[:len(new_list)-1])


if __name__=="__main__":
    num_list = [9,3,4,2,6,7,51]
    new_list = heapsort(num_list)
