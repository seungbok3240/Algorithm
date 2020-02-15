import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tall = list(map(int, input().split()))

left, right = 0, max(tall)

while left <= right:
    mid = (left + right) //2
    total = 0
    for i in tall:
        if i >= mid:
            total = total + (i - mid)
    if total > m:
        left = mid + 1
    elif total < m:
        right = mid - 1
    else:
        print(mid)
        sys.exit()
print(right)
