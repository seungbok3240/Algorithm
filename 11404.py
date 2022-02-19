import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()