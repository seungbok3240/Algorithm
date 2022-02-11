n = int(input())
stack = []

for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)

print(sum(stack))
