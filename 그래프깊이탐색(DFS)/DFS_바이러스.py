v = 0
def DFS(num):
    global v
    visited[num] = True
    for i in connection[num]:
        if not visited[i]:
            v += 1
            DFS(i)


def makenode(n1, n2):
    if n1 not in connection:
        connection[n1] = []
    connection[n1].append(n2)
    if n2 not in connection:
        connection[n2] = []
    connection[n2].append(n1)
    set(connection[n1])
    set(connection[n2])


def printlist(lst):
    for i in range(len(lst)):
        print("->{}".format(lst[i]), end='')


node = int(input("컴퓨터 개수 : "))
edges = int(input("연결된 간선 개수 : "))
connection = {}
for i in range(edges):
    n1, n2 = map(int, input().split())
    makenode(n1, n2)

for key, value in connection.items():
    print("\n정점 {}의 인접 리스트 ".format(key), end = '')
    printlist(value)

print()
visited = {keys:False for keys in connection}
virus = int(input("컴퓨터 번호 : "))
DFS(virus)
print("{}번 컴퓨터와 연결되어 바이러스에 걸린 컴퓨터 {}대".format(virus, v))