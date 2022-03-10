import sys
import re

s = sys.stdin.readline().rstrip()
result = re.sub('([aeiou])p([aeiou])', r'\1', s)
print(result)