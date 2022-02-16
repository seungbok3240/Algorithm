import sys

n = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

stack = []

for c in n:
    stack.append(c)
    if c == t[-1] and ''.join(stack[-len(t):]) == t:
        del stack[-len(t):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')