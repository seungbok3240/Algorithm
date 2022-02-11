n = int(input())

people = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        x1, y1 = people[i]
        x2, y2 = people[j]
        if x1 < x2 and y1 < y2:
            rank += 1
    print(rank, end=' ')
