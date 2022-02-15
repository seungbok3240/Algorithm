while True:
    n = list(input())
    if len(n) == 1 and n[0] == '.':
        exit(0)

    stack = []
    flag = True

    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                flag = False
                break
            if stack[-1] != '(':
                flag = False
                break
            stack.pop()
        elif i == ']':
            if not stack:
                flag = False
                break
            if stack[-1] != '[':
                flag = False
                break
            stack.pop()

    if flag and not stack:
        print('yes')
    else:
        print('no')