import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    tmp = int(input())
    heapq.heappush(cards, tmp)

if len(cards) == 1:
    print(0)
    sys.exit(0)

answer = 0
while len(cards) > 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)

    tmp = c1 + c2
    answer += tmp
    heapq.heappush(cards, tmp)

print(answer)