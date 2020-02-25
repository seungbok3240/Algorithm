'''
0, 1, 2, 3 == 북 동 남 서
'''

#북 동 남 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int, input().split())
y, x, direct = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

while True:
    flag = False
    board[y][x] = 2 #1. 현재 위치를 청소한다.
    for i in range(4):
        tmp_direct = direct - 1 if direct - 1 >= 0 else 3   #턴 레프트!!!
        tmp_x, tmp_y = x + dx[tmp_direct], y + dy[tmp_direct]
        if board[tmp_y][tmp_x] == 0:    #2-a 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
            direct = tmp_direct
            x, y = tmp_x, tmp_y
            flag = True
            break
        else:   #2-b 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            direct = tmp_direct
    if flag:
        continue
    
    tmp_direct = direct - 2 if direct > 1 else direct + 2   #후진!!!
    tmp_x, tmp_y = x + dx[tmp_direct], y + dy[tmp_direct]
    if board[tmp_y][tmp_x] == 1:    #2-d 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        break
    else:
        x,y = tmp_x, tmp_y  #2-c 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.

print(sum(board,[]).count(2))