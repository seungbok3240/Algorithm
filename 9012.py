n = int(input())
for _ in range(n):
    stack = []
    p = list(input())
    flag = True
    for i in p:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                flag = False
                break
    if flag:
        if stack:
            print('NO')
        else:
            print('YES')