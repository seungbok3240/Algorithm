import sys

input = sys.stdin.readline

col, row = map(int, input().split())
maze = [list(map(str, input().rstrip())) for _ in range(col)]


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

q = set([(0, 0, maze[0][0])])
result = 1
while q:
    y, x, checked = q.pop()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny <= -1 or ny >= col or nx <= -1 or nx >= row:
            continue
        if maze[ny][nx] not in checked:
            tmp = checked + maze[ny][nx]
            q.add((ny, nx, tmp))
            result = max(result, len(tmp))

print(result)