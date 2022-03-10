import sys
import re

s = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

findall = re.findall(target, s)
print(len(findall))
