parent = {}

def addparent(num):
    if num not in parent:
        parent[num] = num
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


link = {}
while (1):
    try:
        a, b, v = map(str, input().split())
        addparent(a)
        addparent(b)
        link[a, b] = int(v)
        union(a, b)
    except: break

print(link)
