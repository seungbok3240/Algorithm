from collections import deque

n, k = map(int, input().split())
numbers = deque([i + 1 for i in range(n)])

tmp = list()
while numbers:
    numbers.rotate(-(k - 1))
    tmp.append(str(numbers.popleft()))

result = ', '.join(tmp)
print('<'+result+'>')