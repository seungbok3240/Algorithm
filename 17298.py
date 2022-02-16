n = int(input())
numbers = list(map(int, input().split()))

stack = []
answer = [0] * n
for i in range(n - 1, -1, -1):
    while stack:
        if stack[-1] > numbers[i]:
            answer[i] = stack[-1]
            break
        else:
            stack.pop()

    if not stack:
        answer[i] = -1

    stack.append(numbers[i])

print(*answer)
