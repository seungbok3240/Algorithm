num = int(input())
_list = list(map(int, input().split()))
total = int(input())

if sum(_list) == total:
    print(max(_list))
else:
    low = 0
    high = max(_list)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        tmp = 0
        for i in _list:
            tmp += min(i, mid)
        
        if tmp > total:
            high = mid - 1
        else:
            result = mid
            low = mid + 1

    print(result)