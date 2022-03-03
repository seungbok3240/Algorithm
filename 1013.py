import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

start = 0
end = n - 1
answer = float('inf')
a1, a2 = 0, 0
while start < end:
    tmp = nums[start] + nums[end]

    if abs(tmp) < answer:
        answer = abs(tmp)
        a1, a2 = nums[start], nums[end]

    if tmp < 0:
        start += 1
    else:
        end -= 1

print(a1, a2)