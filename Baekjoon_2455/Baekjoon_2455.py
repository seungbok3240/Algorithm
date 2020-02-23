_in, _out = list(), list()

for i in range(4):
    a,b = map(int,input().split())
    _in.append(b)
    _out.append(a)

result = list()
p = 0
for i in range(4):
    p -= _out[i]
    p += _in[i]
    result.append(p)

result.sort()
print(result[-1])