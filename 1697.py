from collections import deque

n, m = map(int, input().split())


def bfs(v):
    q = deque([v])
    while q:
        x = q.popleft()
        if x == m:
            print(dist[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)


dist = [0] * 100001
bfs(n)
