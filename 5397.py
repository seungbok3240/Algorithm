from collections import deque

n = int(input())
for _ in range(n):
    test = input()
    stack = []
    q = deque([])
    for t in test:
        if t == '<':
            if stack:
                q.appendleft(stack.pop())
        elif t == '>':
            if q:
                stack.append(q.popleft())
        elif t == '-':
            if stack:
                stack.pop()
        else:
            stack.append(t)

    print(''.join(stack) + ''.join(q))
