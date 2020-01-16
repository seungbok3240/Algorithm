import collections

y, x = map(int,input().split())

maze = []
queue = collections.deque([])
visited = [[0]*x for i in range(y)] #최단거리 정보 배열

for i in range(y):
    maze.append(input())

queue.append((0,0))
visited[0][0] = 1


while queue:

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    t = queue.popleft()

    _x = t[0]
    _y = t[1]

    if _x == x - 1 and _y == y - 1:
        print(visited[_y][_x])
        break

    for i in range(4):
        nx = _x + dx[i]
        ny = _y + dy[i]
        if nx < x and nx >= 0 and ny < y and ny >= 0: #index check
            if visited[ny][nx] == 0 and maze[ny][nx] == '1':
                visited[ny][nx] = visited[_y][_x] + 1
                queue.append((nx,ny))