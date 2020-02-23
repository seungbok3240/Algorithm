test = int(input())


def check(queue, importance):
    count = 0
    while queue:
        if queue[0][1] == max(importance):
            if queue[0][0] == m:
                return print(count + 1)
            else:
                importance.remove(queue[0][1])
                queue.pop(0)
                count += 1
        else:
            tmp = queue.pop(0)
            queue.append(tmp)

for i in range(test):
    n,m = map(int, input().split())
    a = list()
    importance = list(map(int, input().split()))
    for i in range(len(importance)):
        a.append([i, importance[i]])
    check(a,importance)