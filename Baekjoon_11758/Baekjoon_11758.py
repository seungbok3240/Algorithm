def ccw(x1,y1,x2,y2,x3,y3):
    check = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    return check

info = []
for i in range(3):
    info.append(list(map(int,input().split())))

info = sum(info,[])
a = ccw(info[0],info[1],info[2],info[3],info[4],info[5])
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)