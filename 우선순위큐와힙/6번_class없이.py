def myheapify(L):
    n = len(L)-1
    for i in range(n, 1, -1):
        n = len(L) - 1
        nodenum = i
        while(nodenum!=0):

            if(L[nodenum]<L[int(nodenum/2)]):
                tmp = L[nodenum]
                L[nodenum] = L[int(nodenum/2)]
                L[int(nodenum/2)] = tmp
            else:
                nodenum=int(nodenum/2)
    return L

if __name__ == '__main__':
    L = [0, 5,4,3,2,1]
    L = myheapify(L)
    print(L)

# l=[1,5,4]
# def f():
#     l[0]=66
#     print(l)
#     return l
#
#
# l=f()
# print(l)l
#
# def f(a):
#     b=50
#     a+=100
#     print(a)
#     print(b)
#     return a
#
# if __name__ == '__main__':
#
#     a=10
#     a=f(a)
#     print(a)
