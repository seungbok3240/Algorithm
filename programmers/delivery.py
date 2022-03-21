"""
https://programmers.co.kr/learn/courses/30/lessons/12978
"""


def solution(N, road, K):
    answer = 0

    graph = [[float('inf')] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = 0

    for r in road:
        if graph[r[0] - 1][r[1] - 1] >= r[2]:
            graph[r[0] - 1][r[1] - 1] = r[2]
        if graph[r[1] - 1][r[0] - 1] >= r[2]:
            graph[r[1] - 1][r[0] - 1] = r[2]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for node in graph[0]:
        if node <= K:
            answer += 1

    return answer