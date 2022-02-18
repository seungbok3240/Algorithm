import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    pn = [input().rstrip() for _ in range(n)]
    pn.sort()

    for i in range(n-1):
        tmp = len(pn[i])
        if pn[i] == pn[i+1][:tmp]:
            print('NO')
            break

    else:
        print('YES')