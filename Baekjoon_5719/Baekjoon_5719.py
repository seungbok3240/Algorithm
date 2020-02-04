import sys, heapq, copy
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')

def solve(adjacent, K):
    prev = [-1] * (len(adjacent))    # predecessor
    dist = [INF] * (len(adjacent))   # source로부터의 최소 거리 배열
    dist[K] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, K])

    while priority_queue:
        # 거리가 제일 작은 노드 선택
        current_dist, here = heapq.heappop(priority_queue)

        # 인접 노드 iteration
        for there, length in adjacent[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])

    return dist, prev

def dfs(here):
    if here == end:
        for i in route:
            if i[1] in tmp[i[0]]:
                tmp[i[0]].pop(i[1])
        return
    for i in range(num_place):
        if adjacent[here][i] != float('inf') and dist[here] + adjacent[here][i] == dist[i]:
            route.append((here, i))
            dfs(i)
            route.pop()

if __name__ == "__main__":
    while True:
        num_place, num_road = map(int, input().split())
        if not num_road:    #문제 조건 중 0 0이 들어오면 시스템 종료
            break
        start, end = map(int, input().split())

        adjacent = [defaultdict(lambda : float('inf')) for _ in range(num_place)]
        route = []
        for _ in range(num_road):
            a, b, p = map(int, input().split())

            # 만약 동일한 경로의 간선이 주어질 경우 적은 비용의 간선 선택
            if b in adjacent[a]:
                adjacent[a][b] = min(adjacent[a][b], p)
            else:
                adjacent[a][b] = p

        dist, prev = solve(adjacent, start)
        tmp = copy.deepcopy(adjacent)
        dfs(start)
        dist, prev = solve(tmp, start) #경로 삭제 후 다익스트라

        #탈출!!!
        #거리가 inf이면 갈 수 없다는 뜻이므로 -1을 출력
        if dist[end] == float('inf'):
            print(-1)
        else:
            print(dist[end])