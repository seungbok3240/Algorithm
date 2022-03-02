import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []
a_s, b_s = 0, 0

while True:
    if a_s == len(a):
        result.extend(b[b_s:])
        break
    elif b_s == len(b):
        result.extend(a[a_s:])
        break

    if a[a_s] < b[b_s]:
        result.append(a[a_s])
        a_s += 1
    else:
        result.append(b[b_s])
        b_s += 1

print(*result, sep=' ')
