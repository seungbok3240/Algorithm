N, jimin, hansu = map(int,input().split())

count = 0
while jimin != hansu:   #처음 대결 했을 때 count가 1인데 0으로 시작했으므로
    jimin = (jimin + 1) // 2
    hansu = (hansu + 1) // 2
    count += 1

print(count)
