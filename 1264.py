import sys
import re

while True:
    s = sys.stdin.readline().rstrip()
    if s == '#':
        break

    tmp = re.findall(r'[aeiouAEIOU]', s)
    print(len(tmp))
