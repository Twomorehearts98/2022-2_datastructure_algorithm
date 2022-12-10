weights = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5),
           (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2),
           (3, 5, 4), (3, 6, 8), (4, 6, 1), (5, 6, 6)]
parent = [i for i in range(7)]
dic = {}
weights.sort(key=lambda t: t[2])  # 가중치 기준으로 정렬
mst = []
N = 7  # 그래프 정점 수

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
        mst.append([i[0],i[1]])
        cost +=i[2]
for i in range(len(parent)):
    print("{} :{}".format(i, parent[i]))
print(mst)
print(cost)
