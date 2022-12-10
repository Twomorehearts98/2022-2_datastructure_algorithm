n, m = map(int, input().split(" "))
lst = [[0]*n for i in range(n)]

for i in range(m):
    a, b=map(int, input().split(" "))
    lst[a][b]=1
    lst[b][a]=1
    print(lst)