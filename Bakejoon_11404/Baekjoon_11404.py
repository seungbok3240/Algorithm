import sys
input = sys.stdin.readline

num_city = int(input())
num_bus = int(input())


city_info = dict()
min_fare = [[float('inf') for i in range(num_city)]for i in range(num_city)]

'''
플로이드 알고리즘을 위한 2차원 배열 만드는 부분
이번 문제의 입력 중 도시에서 도시로 가는 비용이 여러개 입력되므로
그 중 최솟값을 찾기 위해 그래프를 이용하였다.
'''

for i in range(1, num_city + 1):
    city_info[i] = dict()

for i in range(1, num_city+1):
    for j in range(1, num_city+1):
        city_info[i][j] = list()
        city_info[i][j].append(0)
        if i == j:
            min_fare[i - 1][j - 1] = 0

for i in range(num_bus):
    departure, arrival, fare = map(int, input().split())
    city_info[departure][arrival].append(fare)

#여러개의 비용 중 최솟값 찾기   
def _min(input_list):
    if len(input_list) == 1:    #이어지지 않은 부분 -> float('inf')
        return float('inf')
    input_list.remove(0)
    return min(input_list)

for i in range(1, num_city+1):
    for j in range(1, num_city+1):
        if i == j:
            continue
        min_fare[i - 1][j- 1] = _min(city_info[i][j])

#플로이드 워셜 알고리즘
for k in range(num_city):
    for i in range(num_city):
        for j in range(num_city):
            if i == j:
                continue
            else:
                min_fare[i][j] = min(min_fare[i][k] + min_fare[k][j], min_fare[i][j])

#출력
for i in min_fare:
    for j in i:
        if j == float('inf'):   #문제에서 갈 수 없는 도시는 0으로 표시하라고 함
            print(0, end = " ")
        else:
            print(j, end = " ")
    print()