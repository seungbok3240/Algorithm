num = int(input())
a = list(map(int, input().split()))
num2 = int(input())
b = list(map(int, input().split()))

a.sort()
for i in b:
    flag = 0
    low, high = 0, num - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == i and flag == 0:
            flag = 1
            print(1, end=" ")
            break
        elif a[mid] > i:
            high = mid - 1
        else:
            low = mid + 1
    if flag == 0:
        print(0, end=" ")