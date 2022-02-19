import sys

input = sys.stdin.readline

k, n = map(int, input().split())
rope = [int(input()) for _ in range(k)]

start = 1
end = max(rope)

result = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for r in rope:
        cnt += (r // mid)

    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)