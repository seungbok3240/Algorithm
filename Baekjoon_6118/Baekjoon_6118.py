import sys, heapq, copy

input = sys.stdin.readline
INF = float('inf')

def solve(adjacent, K):
    prev = [-1] * (len(adjacent) + 1)    # predecessor
    dist = [INF] * (len(adjacent) + 1)   # source로부터의 최소 거리 배열
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

if __name__ == "__main__":
    num_place, num_loop = map(int, input().split())
    K = 1
    adjacent = [{} for _ in range(num_place + 1)]

    for _ in range(num_loop):
        a, b = map(int, input().split())

        # 만약 동일한 경로의 간선이 주어질 경우 적은 비용의 간선 선택
        if b in adjacent[a]:
            adjacent[a][b] = min(adjacent[a][b], 1)
            adjacent[b][a] = min(adjacent[b][a], 1)
        else:
            adjacent[a][b] = 1
            adjacent[b][a] = 1

    dist, prev = solve(adjacent, K)

    copy_dist = copy.deepcopy(dist)
    copy_dist.sort()
    max_distance = copy_dist[-3]
    count = dist.count(max_distance)
    index = dist.index(max_distance)
    print(index, max_distance, count)