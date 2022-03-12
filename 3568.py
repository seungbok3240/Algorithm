import sys
import re

s = list(map(str, sys.stdin.readline().rstrip().split()))
for i in range(1, len(s)):
    s[i] = s[i][:-1]

r = re.compile('\W')
r2 = re.compile('\w+')

t = s[0]  # type
for i in range(1, len(s)):
    tmp = t
    a = r.findall(s[i])
    b = r2.findall(s[i])
    for j in range(len(a) - 1, -1, -1):
        if a[j] == ']':
            tmp = tmp + '['
        elif a[j] == '[':
            tmp = tmp + ']'
        else:
            tmp = tmp + a[j]
    tmp = tmp + ' ' + b[0] + ';'
    print(tmp)