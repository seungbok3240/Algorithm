import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
parent = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
parent[1] = 1
while q:
    now = q.popleft()

    for i in graph[now]:
        if parent[i] == 0:
            parent[i] = now
            q.append(i)

print(*parent[2:], sep='\n')