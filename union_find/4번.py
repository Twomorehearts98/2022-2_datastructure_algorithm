parent = [i for i in range(7)]


def getParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent[x])
        return parent[x]


def unionParent(x, y):
    x = getParent(x)
    y = getParent(y)

    if x < y:
        parent[y] = getParent(x)
    else:
        parent[x] = getParent(y)


def findParent(x, y):
    x = getParent(x)
    y = getParent(y)

    if x == y:
        return True
    else:
        return False


if __name__ == '__main__':
    print(parent)
    cycle = False

    e = int(input('Edge 개수 : '))
    print("간선 입력")
    idx = 0
    save = 0
    while idx < e:
        print(idx, end=' ')
        a, b = map(int, input().split())

        if getParent(a) == getParent(b):
            cycle = True
            idx += ((b - getParent(b)) - 1)
            save = getParent(b)
            continue
        unionParent(a, b)
        idx += 1
    print(parent)
    idx = getParent(save)
    if cycle:
        print("사이클이 존재합니다 : ")

        while (getParent(idx) == save):
            print(idx, end='')
            idx += 1
