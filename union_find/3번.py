parent = [i for i in range(0,11)]

def getParent(x):
    if parent[x] ==x:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)

    if a<b:
        parent[b]= a
    else:
        parent[a] =b

def findParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a == b:
        return True
    return False

if __name__ == '__main__':
    print(parent)

    unionParent(1, 2)
    unionParent(2,3)
    unionParent(3,4)
    unionParent(5,6)
    unionParent(6, 7)
    unionParent(7,8)
    unionParent(9,10)

    print(parent)
    print("1과 5는 연결이 되어 있나요? : ", findParent(1, 5))
    print("1과 3는 연결이 되어 있나요? : ", findParent(1, 3))
    print("5과 10는 연결이 되어 있나요? : ", findParent(5, 10))
