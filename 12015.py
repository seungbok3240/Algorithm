import sys

input = sys.stdin.readline


def bs(v):
    start = 0
    end = len(lis) - 1
    ret = 10**6
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] >= v:
            if ret > mid:
                ret = mid
            end = mid - 1
        else:
            start = mid + 1

    return ret


n = int(input())
cases = list(map(int, input().split()))
lis = [cases[0]]


for i in range(1, n):
    if lis[len(lis) - 1] < cases[i]:
        lis.append(cases[i])
    else:
        lis[bs(cases[i])] = cases[i]

print(len(lis))

