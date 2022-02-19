import sys

input = sys.stdin.readline

# n = int(input())
# c = set(map(int, input().split()))
# n2 = int(input())
# c2 = list(map(int, input().split()))
#
# for i in c2:
#     if i in c:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


def bs(v):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if c[mid] == v:
            return 1
        elif c[mid] > v:
            end = mid - 1
        else:
            start = mid + 1

    return 0


n = int(input())
c = list(map(int, input().split()))
c.sort()

n2 = int(input())
c2 = list(map(int, input().split()))

for i in c2:
    print(bs(i), end=' ')