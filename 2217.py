n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort()

weight = list()
for i in range(n):
    tmp = rope[i] * (n - i)
    weight.append(tmp)

print(max(weight))
