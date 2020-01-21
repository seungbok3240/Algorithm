import sys
sys.setrecursionlimit(10000) #재귀함수 한계 설정
input = sys.stdin.readline  #readline

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0: #런타임에러 수정 부분
        break

    island = [list(map(int,input().split())) for i in range(m)] #input
    check = [[False]*n for i in range(m)]   #연결되어 있는지 확인

    def dfs(x, y):  #입력 케이스에 대해 섬의 연결을 확인하는 부분
        check[x][y] = True
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if island[nx][ny] == 1 and check[nx][ny] is False:
                dfs(nx, ny)

    count = 0
    for i in range(m):
        for j in range(n):
            if island[i][j] == 1 and check[i][j] is False:
                dfs(i, j)
                count += 1

    print(count)    
