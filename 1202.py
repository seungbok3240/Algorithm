import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
j = []
for _ in range(n):
    weight, price = map(int, input().split())
    heapq.heappush(j, (weight, price))

bags = [int(input()) for _ in range(k)]
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while j and bag >= j[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(j)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not j:
        break
print(answer)
