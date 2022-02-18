from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0


def dfs(v):
    global cnt
    visited[v] = True

    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(cnt - 1)