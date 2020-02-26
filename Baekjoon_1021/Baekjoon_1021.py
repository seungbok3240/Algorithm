size, num = map(int, input().split())

find = list(map(int,input().split()))
source = [i for i in range(1, size + 1)]

def one(_list):
    _list = _list[1:]
    return _list

def two(_list):
    tmp = _list.pop(0)
    _list.append(tmp)
    return _list

def three(_list):
    tmp = _list.pop()
    _list.insert(0,tmp)
    return _list

count = 0
for i in find:
    while i != source[0]:
        _index = source.index(i)
        list_size = len(source)
        if _index > list_size//2:
            count += 1
            source = three(source)
        else:
            count += 1
            source = two(source)
    source = one(source)
print(count)
