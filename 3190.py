import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
maze = [[0] * n for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    maze[y - 1][x - 1] = 1  # 사과

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

l = int(input())
togo = []
for _ in range(l):
    sec, dir = input().split()
    togo.append((int(sec), dir))


q = deque()
y, x = 0, 0
q.append((y, x))
dir = 1
time = 1
maze[0][0] = 2
# 0: 빈 칸, 1: 사과, 2: 뱀
while True:
    y, x = y + dy[dir], x + dx[dir]
    if 0 <= y < n and 0 <= x < n and maze[y][x] != 2:
        if not maze[y][x] == 1:
            temp_y, temp_x = q.popleft()
            maze[temp_y][temp_x] = 0
        maze[y][x] = 2
        q.append((y, x))
        if togo:
            if togo[0][0] == time:
                _, loc = togo.pop(0)
                if loc == 'L':
                    dir = (dir - 1) % 4
                else:
                    dir = (dir + 1) % 4
        time += 1
    else:
        print(time)
        break