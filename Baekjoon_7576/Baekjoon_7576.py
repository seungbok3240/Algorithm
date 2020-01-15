import collections

x, y = map(int, input().split())

tomato = [] #토마토 판
queue = collections.deque([]) #익은 토마토 선별 후 queue에 삽입

unriped = 0 #익지 않은 토마토의 개수

#input
for j in range(y):
    tomato.append(list(map(int,input().split())))
    for i in range(x):
        if tomato[j][i] == 1:   #queue input
            queue.append((i,j))
        elif tomato[j][i] == 0:
            unriped += 1

day = 0

while queue:

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    t = queue.popleft()

    _x = t[0]
    _y = t[1]

    #up dowm left right
    for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]

        if nx >= x or nx < 0 or ny >= y or ny < 0: #index check
            continue
        
        if tomato[ny][nx] != 0:
            continue

        tomato[ny][nx] = tomato[_y][_x] + 1
        queue.append((nx,ny))
        day = max(tomato[ny][nx], day)
        unriped -= 1

if unriped == 0:
    print(day-1)
else:
    print(-1)