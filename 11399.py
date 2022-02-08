n = int(input())
arr = list(map(int, input().split()))

total = 0
arr.sort()
arr.insert(0, 0)

for i in range(len(arr) - 1):
    total += arr[i] + arr[i + 1]
    arr[i + 1] = arr[i] + arr[i + 1]

print(total)