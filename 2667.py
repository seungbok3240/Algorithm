def dfs(y, x):
    global count
    if y <= -1 or y >= n or x <= -1 or x >= n:
        return False

    if graph[y][x] == 1:
        count += 1
        graph[y][x] = 0

        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y, x + 1)
        return True

    return False


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

count = 0
c = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            c.append(count)
            count = 0

c.sort()
print(len(c))
print(*c, sep='\n')