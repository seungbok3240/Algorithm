import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'pop':
        if stack:
            tmp = stack.pop()
            print(tmp)
        else:
            print(-1)
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)