import sys

while True:
    try:
        x = int(sys.stdin.readline()) * (10 ** 7)
    except:
        break
    num = int(sys.stdin.readline())

    rego = list()
    for i in range(num):
        rego.append(int(sys.stdin.readline()))

    rego.sort()
    
    start, end= 0, len(rego)-1
    while start < end:
        _sum = rego[start] + rego[end]
        if _sum == x:
            print("yes",rego[start], rego[end])
            break
        if _sum < x:
            start += 1
        else:
            end -= 1
    if start >= end:
        print("danger")