import sys
from collections import deque

init = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if init:
            queue.appendleft(init.pop())
    elif command[0] == 'D':
        if queue:
            init.append(queue.popleft())
    elif command[0] == 'B':
        if init:
            init.pop()
    elif command[0] == 'P':
        init.append(command[1])

print(''.join(init)+''.join(queue))