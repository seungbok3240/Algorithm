import sys

n = sys.stdin.readline().rstrip()

t = 'PPAP'
stack = []
for c in n:
    stack.append(c)
    if len(stack) >= 4 and c == t[-1] and ''.join(stack[-len(t):]) == t:
        del stack[-len(t):]
        stack.append('P')

if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')