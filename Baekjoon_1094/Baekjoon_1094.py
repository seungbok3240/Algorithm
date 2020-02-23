x = int(input())

a = list()
a.append(64)

_sum = 64
while _sum > x:
    tmp = a.pop(0) // 2
    a.append(tmp)
    if sum(a) >= x:
        pass
    else:
        a.append(tmp)
    a.sort()
    _sum = sum(a)

print(len(a))