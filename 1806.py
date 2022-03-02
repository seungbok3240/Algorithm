import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
mid_sum = 0
result = float('inf')
for start in range(n):
    while mid_sum < m and end < n:
        mid_sum += nums[end]
        end += 1

    if mid_sum >= m:
        result = min(result, end - start)

    mid_sum -= nums[start]

if result == float('inf'):
    print(0)
else:
    print(result)
