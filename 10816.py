import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
c.sort()
n2 = int(input())
c2 = list(map(int, input().split()))


for i in c2:
    left = bisect_left(c, i)
    right = bisect_right(c, i)

    print(right - left, end=' ')