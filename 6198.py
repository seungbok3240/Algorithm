import sys

n = int(sys.stdin.readline().rstrip())
height = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

stack = []
cnt = 0
for h in height:
    while stack and stack[-1] < h:
        stack.pop()
    stack.append(h)
    cnt += len(stack) - 1

print(cnt)
