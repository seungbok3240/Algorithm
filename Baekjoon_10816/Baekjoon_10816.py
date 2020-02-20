from collections import Counter
import bisect

num = int(input())
a = list(map(int,input().split()))
num2 = int(input())
b = list(map(int,input().split()))

c= Counter(a)

for i in b:
    print(c[i], end=' ')