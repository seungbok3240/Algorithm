import sys

try:
    n = input()

    stack = []
    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack[-1] = 2
                else:
                    tmp = 0
                    for j in range(len(stack) - 1, -1, -1):
                        if stack[j] == '(':
                            stack[-1] = tmp * 2
                            break
                        else:
                            tmp += stack[j]
                            stack = stack[:-1]
            else:
                print(0)
                sys.exit(0)
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack[-1] = 3
                else:
                    tmp = 0
                    for j in range(len(stack) - 1, -1, -1):
                        if stack[j] == '[':
                            stack[-1] = tmp * 3
                            break
                        else:
                            tmp += stack[j]
                            stack = stack[:-1]
            else:
                print(0)
                sys.exit(0)

    print(sum(stack))
except TypeError:
    print(0)
