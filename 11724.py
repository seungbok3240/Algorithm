import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**5)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return True


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i):
            cnt += 1
print(cnt)
