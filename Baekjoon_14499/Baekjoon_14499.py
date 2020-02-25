import copy

n,m,y,x,k = map(int,input().split())
board = [list(map(int,input().split())) for i in range(n)]
mission = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

def checkBoard(x,y):
    if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0:
        return True
    else:
        return False

def rolldice(dice,i):
    tmp_dice = copy.deepcopy(dice)
    if i == 1:  #동
        dice[-1] = tmp_dice[2]
        dice[2] = tmp_dice[0]
        dice[0] = tmp_dice[3]
        dice[3] = tmp_dice[-1]
    elif i == 2:    #서
        dice[-1] = tmp_dice[3]
        dice[3] = tmp_dice[0]
        dice[0] = tmp_dice[2]
        dice[2] = tmp_dice[-1]
    elif i == 3:    #북
        dice[0] = tmp_dice[4]
        dice[4] = tmp_dice[-1]
        dice[-1] = tmp_dice[1]
        dice[1] = tmp_dice[0]
    else:   #남
        dice[0] = tmp_dice[1]
        dice[1] = tmp_dice[-1]
        dice[-1] = tmp_dice[4]
        dice[4] = tmp_dice[0]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def check(x,y,dice,i):
    x += dx[i - 1]
    y += dy[i - 1]
    if checkBoard(x,y):
        x -= dx[i - 1]
        y -= dy[i - 1]
        return x, y, dice, 0
    rolldice(dice,i)
    if board[y][x] == 0:
        board[y][x] = dice[-1]
    else:
        dice[-1] = board[y][x]
        board[y][x] = 0
    return x, y, dice, 1

for i in mission:
    if i == 1:  #동
        x, y, dice, flag = check(x,y,dice,i)
        if flag == 1:
            print(dice[0])
    elif i == 2:    #서
        x, y, dice, flag = check(x,y,dice,i)
        if flag == 1:
            print(dice[0])
    elif i == 3:    #북
        x, y, dice, flag = check(x,y,dice,i)
        if flag == 1:
            print(dice[0])
    else:   #남
        x, y, dice, flag = check(x,y,dice,i)
        if flag == 1:
            print(dice[0])