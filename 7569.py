import sys
from collections import deque

input = sys.stdin.readline

w, h, u = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(h)] for _ in range(u)]
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()
for i in range(u):
    for j in range(h):
        for k in range(w):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

while q:
    z, y, x = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if nz <= -1 or nz >= u or ny <= -1 or ny >= h or nx <= -1 or nx >= w:
            continue
        if tomato[nz][ny][nx] == 0:
            tomato[nz][ny][nx] = tomato[z][y][x] + 1
            q.append((nz, ny, nx))

answer = 0
for i in tomato:
    for j in i:
        if 0 in j:
            print(-1)
            sys.exit(0)
        answer = max(answer, max(j))

print(answer - 1)
