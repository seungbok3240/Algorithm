import sys

input = sys.stdin.readline

n = int(input())

a = [0, 1, 2]

for i in range(3, n + 1):
    a.append(a[i-2] + a[i-1])

print(a[n] % 10007)
