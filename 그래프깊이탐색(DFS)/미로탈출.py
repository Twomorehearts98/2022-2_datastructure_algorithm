row, line = map(int, input('size : ').split())
print('행열 자료입력')
matrix = [list(map(int, input().split())) for k in range(row)]
cnt = 0
way = []
sw=0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    global sw, cnt
    if x == a and y == b:
        sw=1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0 <= ny < line and matrix[nx][ny] == 0 and sw == 0:
            matrix[nx][ny] =1
            way.append([nx, ny])
            cnt+=1
            dfs(nx, ny)
            matrix[nx][ny] = 0
            #way.pop()


nums = 0
g = 0
a, b = map(int, input("도착지점").split())

dfs(0, 0)
if sw == 1:
    print(way)
    print(cnt)
else:
    print("no way")