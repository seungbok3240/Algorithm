import sys
from collections import deque


def bfs():
    while q:
        i, j = q.popleft()

        for index in range(4):
            ny = i + dy[index]
            nx = j + dx[index]

            if ny <= - 1 or ny >= n or nx <= -1 or nx >= m:
                continue

            if tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[i][j] + 1
                q.append((ny, nx))


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

bfs()
answer = 0
for i in tomato:
    if 0 in i:
        print(-1)
        sys.exit()
    else:
        answer = max(answer, max(i))

print(answer - 1)