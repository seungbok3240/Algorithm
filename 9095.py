import sys

input = sys.stdin.readline


def a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return a(n - 1) + a(n - 2) + a(n - 3)


t = int(input())
for _ in range(t):
    n = int(input())
    print(a(n))
