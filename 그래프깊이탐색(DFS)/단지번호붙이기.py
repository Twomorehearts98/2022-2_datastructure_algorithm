# def makenum(m, n, count):
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     for i in range(4):
#         if visited[m][n] == False and matrix[m][n] == 1:
#             visited[m][n] = True
#             if homedict == {}:
#                 homedict[count] = []
#             homedict[count].append([m, n])
#         else:
#             count += 1
#         makenum(m + dx[i], n + dy[i], count)
#
#
# # size = int(input("size: "))
# size = 7
# homedict = {}
# # matrix = [list(map(int, input().split())) for i in range(size)]
# matrix = [[0, 1, 1, 0, 1, 0, 0],
#           [0, 1, 1, 0, 1, 0, 1],
#           [1, 1, 1, 0, 1, 0, 1],
#           [0, 0, 0, 0, 1, 1, 1],
#           [0, 1, 0, 0, 0, 0, 0],
#           [0, 1, 1, 1, 1, 1, 0],
#           [0, 1, 1, 1, 0, 0, 0]]
# visited = [[False for j in range(size)] for k in range(size)]
#
# makenum(0, 0, 1)
#
# for key, value in homedict.items():
#     print("{}단지 가구 수 : {}".format(key, len(value)))

# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
size = int(input('size : '))
visited = [[0] * (size) for i in range(size + 1)]
matrix = [[0] * (size) for i in range(size)]

print('행열 자료입력')
for i in range(size):
    l = input()
    for k in range(size):
        matrix[i][k] = int(l[k])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = 1
    global nums
    if matrix[x][y] == 1:
        nums += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < size and 0 <= ny < size:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny)


nums = 0
g = 0
for a in range(size):
    for b in range(size):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a, b)
            g += 1
            print('{}단지 가구수 : {}'.format(g, nums))
            nums = 0

print('단지수 :', g)
