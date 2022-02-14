from itertools import combinations


def cal_dist(i, j, c): # 거리 구하기
    return abs(i - c[0]) + abs(j - c[1])


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

chicken = list()
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))  # 치킨집 리스트

predicted = list(combinations(chicken, m))  # m개 조합
chicken_dist = []
for p in predicted:
    chicken_dist_tmp = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                chicken_to_house = []
                for k in range(m):
                    t = cal_dist(i, j, p[k])
                    chicken_to_house.append(t)
                min_dist = min(chicken_to_house)
                chicken_dist_tmp.append(min_dist)
    chicken_dist.append(sum(chicken_dist_tmp))
print(min(chicken_dist))