import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
now_y, now_x, see = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

sight = [0, 1, 2, 3]

q = deque()
q.append((now_y, now_x, see, 0))
result = 0
while q:
    y, x, s, cnt = q.popleft()
    if cnt == 4:
        if s == 0:
            if 0 <= y + 1 <= n and 0 <= x <= m and maze[y + 1][x] != 1:
                q.append((y + 1, x, s, 0))
            else:
                break
        elif s == 1:
            if 0 <= y <= n and 0 <= x - 1 <= m and maze[y][x - 1] != 1:
                q.append((y, x - 1, s, 0))
            else:
                break
        elif s == 2:
            if 0 <= y - 1 <= n and 0 <= x <= m and maze[y - 1][x] != 1:
                q.append((y - 1, x, s, 0))
            else:
                break
        elif s == 3:
            if 0 <= y <= n and 0 <= x + 1 <= m and maze[y][x + 1] != 1:
                q.append((y, x + 1, s, 0))
            else:
                break

    if maze[y][x] == 0:
        result += 1
        maze[y][x] = 2  # 청소완료

    if s == 0:
        if 0 <= y <= n and 0 <= x - 1 <= m:
            if maze[y][x - 1] == 0:
                q.append((y, x - 1, sight[s - 1], 0))
            else:
                q.append((y, x, sight[s - 1], cnt + 1))
    elif s == 1:
        if 0 <= y - 1 <= n and 0 <= x <= m:
            if maze[y - 1][x] == 0:
                q.append((y - 1, x, sight[s - 1], 0))
            else:
                q.append((y, x, sight[s - 1], cnt + 1))
    elif s == 2:
        if 0 <= y <= n and 0 <= x + 1 <= m:
            if maze[y][x + 1] == 0:
                q.append((y, x + 1, sight[s - 1], 0))
            else:
                q.append((y, x, sight[s - 1], cnt + 1))
    elif s == 3:
        if 0 <= y + 1 <= n and 0 <= x <= m:
            if maze[y + 1][x] == 0:
                q.append((y + 1, x, sight[s - 1], 0))
            else:
                q.append((y, x, sight[s - 1], cnt + 1))

print(result)