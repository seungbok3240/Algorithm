n = int(input())
answer = [int(input()) for _ in range(n)]

stack = []
result = []
i = 1
answer_index = 0
while True:
    if stack and stack[-1] == answer[answer_index]:
        stack.pop()
        result.append('-')
        answer_index += 1
    else:
        if i == n + 1:
            break
        stack.append(i)
        result.append('+')
        i += 1

if stack:
    print('NO')
else:
    print('\n'.join(result))
