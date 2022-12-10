depth_list = [0]
graph = {
    1:[2,3],
    2:[1,4,5],
    3:[1],
    4:[2,6],
    5:[2],
    6:[4]
}


def dfs(num, depth, discovered=[]):
    discovered.append(num)
    for w in graph[num]:
        if not w in discovered:
            depth_list.append(depth)
            discovered = dfs(w, depth+1, discovered)
    return discovered


if __name__ == "__main__":
    i = []
    n = 1
    while 1:
        print("{}와 연결된 노드 : ".format(n), end='')
        i = list(map(int, input().split()))
        if -1 in i:
            break
        graph[n] = i
        n += 1
    result = dict(zip(dfs(1,1),depth_list))

    for key, value in result.items():
        print("{}의 깊이 : {}".format(key, value))