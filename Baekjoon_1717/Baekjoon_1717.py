import sys
sys.setrecursionlimit(10**6)

def find(index):
    if index != data[index]:
        data[index] = find(data[index])
    return data[index]

def union(x,y):
    data[find(y)] = find(x)

a, b = map(int, sys.stdin.readline().split())
data = list(range(a + 1))
for i in range(b):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0:
        union(y - 1,z - 1)
    else:
        if find(y-1) == find(z-1):
            print("YES")
        else:
            print("NO")