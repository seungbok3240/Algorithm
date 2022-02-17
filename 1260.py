from collections import defaultdict, deque


def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = defaultdict(list)
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i] = sorted(graph[i])

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)

