import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))


def dijkstra(start):
    distance = [float('inf')] * (n + 1)

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


result = 0
for i in range(1, n + 1):
    s = dijkstra(i)
    e = dijkstra(x)
    result = max(result, s[x] + e[i])
print(result)