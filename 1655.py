import sys
import heapq

input = sys.stdin.readline

n = int(input())
q1 = []
q2 = []
for _ in range(n):
    x = int(input())

    if len(q1) == len(q2):
        heapq.heappush(q1, -x)
    else:
        heapq.heappush(q2, x)

    print(q1, q2)

    if q1 and q2 and -q1[0] > q2[0]:
        tmp1 = -heapq.heappop(q1)
        tmp2 = heapq.heappop(q2)

        heapq.heappush(q1, -tmp2)
        heapq.heappush(q2, tmp1)

    print(-q1[0])
