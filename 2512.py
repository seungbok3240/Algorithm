import sys

input = sys.stdin.readline

n = int(input())
money = list(map(int, input().split()))
m = int(input())


start = 0
end = max(money)
result = 0
while start <= end:
    mid = (start + end) // 2

    total = m
    for i in money:
        if i > mid:
            total = total - mid
        else:
            total = total - i

    if total == 0:
        result = mid
        break
    elif total < 0:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
