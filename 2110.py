import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
answer = 0
while start <= end:
    mid = (start + end) // 2

    now = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] >= now + mid:
            cnt += 1
            now = house[i]

    if cnt >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)