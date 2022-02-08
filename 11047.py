n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)

cnt = 0
for c in coin:
    if c > k:
        continue

    cnt += k // c
    k = k % c

print(cnt)