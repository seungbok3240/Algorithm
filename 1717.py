import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    flag, a, b = map(int, input().split())
    if not flag:
        union_parent(parent, a, b)
    else:
        x = find_parent(parent, a)
        y = find_parent(parent, b)
        if x == y:
            print('YES')
        else:
            print('NO')