# if __name__ == "__main__":
#     n, m = map(int, input().split(" "))
#     lst = [[] for i in range(n)]
#     for i in range(n):
#         lst[i].append(i)
#
#     for i in range(m):
#         a, b = map(int, input().split(" "))
#         lst[a].append(b)
#         lst[b].append(a)
#
#     for i in lst:
#         print("{0} : ".format(i[0]), end='')
#         for j in range(1, len(i)):
#             print(i[j], end=' ')
#         print()
dic={}
n, m = map(int, input().split(" "))
for i in range(n):
    dic[i]=[]
for i in range(m):
    a, b = map(int, input().split(" "))
    dic[a].append(b)
    dic[b].append(a)

print(dic)
