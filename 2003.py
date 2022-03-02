import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
cnt = 0
interval_sum = 0
for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += nums[end]
        end += 1

    if interval_sum == m:
        cnt += 1
    interval_sum -= nums[start]

print(cnt)
