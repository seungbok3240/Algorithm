import sys

input = sys.stdin.readline

num = int(input())
a = set(map(int, input().split()))
num2 = int(input())
b = list(map(int, input().split()))
for i in b:
    if i in a:
        print(1)
    else:
        print(0)