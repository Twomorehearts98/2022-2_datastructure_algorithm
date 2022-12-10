weights = [('E', 'G', 2), ('A', 'B', 3), ('E', 'F', 4), ('B', 'D', 5),
           ('A', 'D', 6), ('C', 'F', 8), ('D', 'E', 9), ('C', 'E', 10),
           ('B', 'G', 12), ('F', 'G', 14), ('A', 'C', 17)]
parent = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G'}
dic = {}
weights.sort(key=lambda t: t[2])  # 가중치 기준으로 정렬
mst = []


def find(u):
    if u != parent[u]:
        return find(parent[u])
    return parent[u]


def union(u, v):  # union 연산
    root1 = find(u)
    root2 = find(v)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


cycle = False
mst = []
cost = 0
for i in weights:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        mst.append([i[0], i[1]])
        cost += i[2]
print(mst)
print(cost)
