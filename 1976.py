import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())
m = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

parent = [0] * n
for i in range(n):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if maze[i][j] == 1:
            union_parent(parent, i, j)


result = set()
for i in plan:
    tmp = find_parent(parent, i - 1)
    result.add(tmp)

if len(result) == 1:
    print('YES')
else:
    print('NO')