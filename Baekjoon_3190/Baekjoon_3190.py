import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0 for i in range(N)]for i in range(N)]

for i in range(K):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    board[y][x] = 2 #사과

L = int(input())
move = []
for i in range(L):
    sec, way = input().split()
    sec = int(sec)
    move.append([sec,way])
move.append([N*N,'L'])  #밑에서 for문을 돌 때 주어진 뱀의 이동경로를 다 돌고 나서 그 방향으로 계속 나아가기 위함
#0 1 2 3
#북동남서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

queue = []  #뱀 좌표
head = 1
count = 0
x, y = 0, 0
queue.append([0,0]) #맨 처음 뱀의 위치
board[0][0] = 5 #뱀은 5로 표시
for info in move:
    while True:
        x += dx[head]
        y += dy[head]
        if x < 0 or y < 0 or x >= N or y >= N:  #뱀이 밖으로 나갔을 때
            print(count + 1)
            sys.exit()
        elif [y,x] in queue:    #뱀이 자신의 몸과 충돌하였을 때
            print(count + 1)
            sys.exit()
        else:
            if board[y][x] == 2:    #사과를 먹은 경우
                count += 1
                board[y][x] = 5
                queue.append([y,x])
            else:                   #빈 칸인 경우
                count += 1
                board[y][x] = 5
                prev = queue.pop(0)
                board[prev[0]][prev[1]] = 0
                queue.append([y,x])
            if count == info[0]:    #뱀의 이동경로가 바뀌는 경우
                if info[1] == 'L':
                    head = (head + 3) % 4
                    break
                else:
                    head = (head + 1) % 4
                    break