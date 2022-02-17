from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))
c = Counter(numbers)

stack = []
answer = [-1] * n
for i in range(n):
    while stack and c[numbers[stack[-1]]] < c[numbers[i]]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)
