from collections import deque


def bfs(graph, x, y):
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))


n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

bfs(maze, 0, 0)

print(maze[n - 1][m - 1])