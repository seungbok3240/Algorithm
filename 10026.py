import sys
import copy

sys.setrecursionlimit(10**5)
r = sys.stdin.readline


def dfs(y, x, tmp_picture, target):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <= -1 or ny >= n or nx <= -1 or nx >= n:
            continue
        if not tmp_picture[ny][nx].isdigit() and tmp_picture[ny][nx] == target:
            tmp_picture[ny][nx] = '1'
            dfs(ny, nx, tmp_picture, target)


n = int(input())
picture = [list(r().rstrip()) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

tmp_picture = copy.deepcopy(picture)
cnt = 0
for target in ('R', 'G', 'B'):
    for i in range(n):
        for j in range(n):
            if not tmp_picture[i][j].isdigit() and tmp_picture[i][j] == target:
                tmp_picture[i][j] = '1'
                dfs(i, j, tmp_picture, target)
                cnt += 1

for i in range(n):
    for j in range(n):
        if picture[i][j] == 'R':
            picture[i][j] = 'G'

cnt2 = 0
for target in ('G', 'B'):
    for i in range(n):
        for j in range(n):
            if not picture[i][j].isdigit() and picture[i][j] == target:
                picture[i][j] = '1'
                dfs(i, j, picture, target)
                cnt2 += 1

print(cnt, cnt2)