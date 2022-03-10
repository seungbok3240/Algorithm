import sys
import re

input = sys.stdin.readline

r = re.compile('\d+')
n = int(input())
numbers = []
for _ in range(n):
    target = input().rstrip()
    tmp = r.findall(target)
    numbers.extend(list(map(int, tmp)))

numbers.sort()
print(*numbers, sep='\n')