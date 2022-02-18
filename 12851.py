from collections import deque

n, m = map(int, input().split())


def bfs(v):
    global cnt
    q = deque([v])
    dist[v] = 0

    while q:
        x = q.popleft()
        if x == m:
            cnt += 1
        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= 100000:
                if dist[i] == -1 or dist[i] == dist[x] + 1:
                    dist[i] = dist[x] + 1
                    q.append(i)


cnt = 0
dist = [-1] * 100001
bfs(n)
print(dist[m])
print(cnt)
