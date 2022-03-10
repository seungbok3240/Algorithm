import sys
import re

r = re.compile('FBI')

flag = True
for i in range(5):
    target = sys.stdin.readline().rstrip()
    result = r.search(target)
    if result is not None:
        flag = False
        print(i + 1, end=' ')

if flag:
    print('HE GOT AWAY!')
