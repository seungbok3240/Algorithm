n = int(input())
time = [tuple(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x: (x[1], x[0]))

now = time[0]

cnt = 1
for i in range(1, len(time)):
    if now[1] <= time[i][0]:
        now = time[i]
        cnt += 1

print(cnt)
