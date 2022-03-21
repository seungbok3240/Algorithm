import sys
import re

input = sys.stdin.readline

gather = re.compile('[aeiou]')
isTriple = re.compile('[aeiou]{3}|[^aeiou]{3}')
isDouble = re.compile(r'([^e|o|\s])\1')

while True:
    s = input().rstrip()
    if s == 'end':
        break

    g = gather.findall(s)
    t = isTriple.findall(s)
    d = isDouble.findall(s)

    if g and not t and not d:
        print('<{}> is acceptable.'.format(s))
    else:
        print('<{}> is not acceptable.'.format(s))
