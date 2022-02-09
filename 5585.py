n = 1000 - int(input())

coin = [500, 100, 50, 10, 5, 1]

cnt = 0
for c in coin:
    if n < c:
        continue
    else:
        cnt += n // c
        n = n % c

print(cnt)
