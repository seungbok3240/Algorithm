import sys, copy

sys.setrecursionlimit(10**5)


def dfs(y, x):
    tmp_island[y][x] = 101

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <= -1 or ny >= n or nx <= - 1 or nx >= n:
            continue

        if tmp_island[ny][nx] < 101:
            dfs(ny, nx)


n = int(sys.stdin.readline().rstrip())
island = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_height = 0
for i in island:
    max_height = max(max_height, max(i))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
count = []
for i in range(1, max_height + 1):
    tmp_island = copy.deepcopy(island)
    for j in range(n):
        for k in range(n):
            if tmp_island[j][k] < i:
                tmp_island[j][k] = 101

    cnt = 0
    for j in range(n):
        for k in range(n):
            if tmp_island[j][k] < 101:
                dfs(j, k)
                cnt += 1

    count.append(cnt)

print(max(count))