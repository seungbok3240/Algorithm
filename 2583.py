import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

col, row, k = map(int, input().split())
graph = [[0] * row for _ in range(col)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    global g_cnt
    if y <= - 1 or y >= col or x <= - 1 or x >= row:
        return False

    if graph[y][x] == 0:
        g_cnt += 1
        graph[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(ny, nx)
        return True

    return False


cnt = []
g_cnt = 0
for i in range(col):
    for j in range(row):
        if dfs(i, j):
            cnt.append(g_cnt)
            g_cnt = 0

print(len(cnt))
cnt.sort()
print(*cnt)