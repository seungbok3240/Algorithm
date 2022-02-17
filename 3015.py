n = int(input())
people = [int(input()) for _ in range(n)]

stack = []
answer = 0
for c in people:
    while stack and stack[-1][0] < c:
        answer += stack.pop()[1]
    if not stack:
        stack.append((c, 1))
        print(stack)
        continue

    if stack[-1][0] == c:
        tmp = stack.pop()[1]
        answer += tmp

        if stack:
            answer += 1
        stack.append((c, tmp + 1))
    else:
        stack.append((c, 1))
        answer += 1
    print(stack)

print(answer)