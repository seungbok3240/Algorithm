import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline


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


n, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

one, two = map(int, input().split())


a = dijkstra(1)
b = dijkstra(one)
c = dijkstra(two)

result = min(a[one] + b[two] + c[n], a[two] + c[one] + b[n])
if result != float('inf'):
    print(result)
else:
    print(-1)
