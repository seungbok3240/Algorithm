problem = str(input())
problem = problem.replace('()', '*')

result = 0
stack = []
for i in problem:
    if i == '*':
        result += len(stack)
    elif i == '(':
        stack.append('(')
    elif i == ')':
        stack.pop()
        result += 1

print(result)