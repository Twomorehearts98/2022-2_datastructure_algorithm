adj_list = [[2, 1], [3, 1], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7,5], [6, 5], [3], [3]]
N = len(adj_list)
visited = [False for x in range(N + 1)]
def dfs(v):
    visited[v] = True
    print(v, ' ', end = ' ')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


print('DFS방문순서 : ', end = '')
for i in range(N):
    if not visited[i]:
        dfs(i)
        print()
# dfs(0)