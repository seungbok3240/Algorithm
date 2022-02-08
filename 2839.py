n = int(input())

cnt = 0
while True:
    if n % 5 == 0:
        print(n // 5 + cnt)
        exit(0)

    n -= 3
    cnt += 1
    # if n == 0:
    #     print(cnt)
    #     exit(0)

    if n < 0:
        print(-1)
        exit(0)