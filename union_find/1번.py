adj_list = [[1, 2], [0], [0], [4], [3]]

N = len(adj_list)

CCList = []
visited = [False for x in range(N + 1)]

def dfs(v):
    visited[v] = True
    cc.append(v)
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


for i in range(N):
    if not visited[i]:
        cc = []
        dfs(i)
        CCList.append(cc)

print("연결성분 리스트:")
print(CCList)
