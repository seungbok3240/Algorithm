import sys

sys.setrecursionlimit(10**5)


def dfs(y, x):
    island[y][x] = 3

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny <= -1 or ny >= h or nx <= -1 or nx >= w:
            continue
        if island[ny][nx] == 1:
            dfs(ny, nx)


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        sys.exit(0)
    island = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]

    dy = [0, 0, 1, -1, -1, -1, 1, 1]
    dx = [1, -1, 0, 0, -1, 1, -1, 1]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
