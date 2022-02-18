import sys

sys.setrecursionlimit(10**5)


def dfs(y, x):
    if y <= -1 or y >= n or x <= -1 or x >= m:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(ny, nx)

        return True
    return False


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    print(cnt)
