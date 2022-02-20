import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1
while q:
    y, x, flag = q.popleft()
    if y == n - 1 and x == m - 1:
        print(visited[y][x][flag])
        sys.exit(0)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
            continue

        if not visited[ny][nx][flag]:
            if maze[ny][nx] == 1 and not flag:
                visited[ny][nx][flag + 1] = visited[y][x][flag] + 1
                q.append((ny, nx, flag + 1))
            elif maze[ny][nx] == 0:
                visited[ny][nx][flag] = visited[y][x][flag] + 1
                q.append((ny, nx, flag))

print(-1)