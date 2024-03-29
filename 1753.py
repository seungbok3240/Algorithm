import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [float('inf')] * (V + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print('INF', end=' ')
    else:
        print(distance[i], end=' ')