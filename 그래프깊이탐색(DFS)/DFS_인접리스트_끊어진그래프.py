import random

def DFS(char):
    if visited[char] == False:
        visited[char] = True
        print(char, ' ', end=' ')
        for i in connection[char]:
            if not visited[i]:
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


node = int(input("정점 개수 : "))
edges = int(input("Edge 개수 : "))
connection = {}
for i in range(edges):
    n1, n2 = map(str, input("Edge (양방향) :").split())
    makenode(n1, n2)

for key, value in connection.items():
    print("\n정점 {}의 인접 리스트 ".format(key), end = '')
    printlist(value)

print()
visited = {keys:False for keys in connection}
print(visited)
for i in visited:
    if visited[i] == False:
        DFS(i)