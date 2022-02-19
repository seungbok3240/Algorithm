import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(m)]


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited = [[-1] * n for _ in range(m)]
q = deque([(0, 0)])
visited[0][0] = 0

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <= -1 or ny >= m or nx <= -1 or nx >= n:
            continue

        if visited[ny][nx] == -1:
            if maze[ny][nx] == 0:
                visited[ny][nx] = visited[y][x]
                q.appendleft((ny, nx))
            else:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))


print(visited[m - 1][n - 1])