import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    arr = list(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = []

    flag = True
    out = 0
    for c in p:
        if c == 'R':
            flag = not flag
        elif c == 'D':
            if arr:
                if flag:
                    arr.pop(0)
                else:
                    arr.pop()
            else:
                print('error')
                out = 1
                break

    if out == 0:
        if flag:
            result = '['
            result += ','.join(arr)
            result += ']'
            print(result)
        else:
            result = '['
            result += ','.join(arr[::-1])
            result += ']'
            print(result)
