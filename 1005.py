import sys
from collections import deque

input = sys.stdin.readline


def topology_sort(target):
    result = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, times[i]))

    while q:
        now, n_t = q.popleft()

        if now == target:
            return n_t

        for i in graph[now]:
            result[i] = max(result[i], n_t + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, result[i]))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    times.insert(0, 0)

    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    target = int(input())

    answer = topology_sort(target)
    print(answer)
