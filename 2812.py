n, k = map(int, input().split())
number = list(input())

tmp = n - k
stack = []
for i in range(n):
    while k > 0 and stack:
        if stack[-1] < number[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(number[i])

for i in range(tmp):
    print(stack[i], end='')