import sys

case = sys.stdin.readline().rstrip()

stack = []
for s in case:
    if s == '(':
        stack.append(s)
    elif s == ')':
        tmp = 0
        while stack and stack[-1] != '(':
            if type(stack[-1]) is int:
                tmp += stack.pop()
            else:
                tmp += len(stack.pop())
        stack.pop()
        stack[-1] = int(stack[-1]) * tmp
    else:
        stack.append(s)

result = 0
for i in stack:
    if type(i) is str:
        result += len(i)
    else:
        result += i

print(result)
