house, wifi = map(int,input().split())

_list = list()
for i in range(house):
    _list.append(int(input()))

_list.sort()

def check(mid):
    count = 1   #_list[0]에 공유기를 설치하고 시작하므로 1로 초기화
    now = _list[0]
    for i in range(1,len(_list)):
        if _list[i] - now >= mid:
            count += 1
            now = _list[i]
    if count >= wifi:
        return True
    else:
        return False

left, right = 1, _list[-1] - _list[0]   #최소거리, 최대거리
result = 0
while left <= right:
    mid = (left + right) //2
    if check(mid):
        result  = max(result,mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)