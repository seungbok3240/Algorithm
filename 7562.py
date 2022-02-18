import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

t = int(input())
for _ in range(t):
    n = int(input())
    y, x = map(int, input().split())
    target_y, target_x = map(int, input().split())

    visited = [[0] * n for _ in range(n)]

    q = deque([(y, x)])
    visited[y][x] = 1
    while q:
        a, b = q.popleft()
        if a == target_y and b == target_x:
            break

        for i in range(8):
            ny = a + dy[i]
            nx = b + dx[i]

            if ny <= -1 or ny >= n or nx <= -1 or nx >= n:
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[a][b] + 1
                q.append((ny, nx))

    print(visited[target_y][target_x] - 1)