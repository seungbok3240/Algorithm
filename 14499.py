import sys
from collections import defaultdict

input = sys.stdin.readline

col, row, y, x, k = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(col)]
command = list(map(int, input().split()))

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
dice = [0] * 6


def turn(dir):
    one, two, three, four, five, six = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = four, two, one, six, five, three
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = three, two, six, one, five, four
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = five, one, three, four, six, two
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = two, six, three, four, one, five


ny, nx = y, x
for i in command:
    ny = ny + dy[i - 1]
    nx = nx + dx[i - 1]

    if 0 <= ny < col and 0 <= nx < row:
        turn(i)
        if maze[ny][nx] == 0:
            maze[ny][nx] = dice[-1]
        else:
            dice[-1] = maze[ny][nx]
            maze[ny][nx] = 0
    else:
        ny, nx = ny - dy[i - 1], nx - dx[i - 1]
        continue

    print(dice[0])
