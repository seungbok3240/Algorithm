import sys

input = sys.stdin.readline

_input, target = map(int, input().split())

monster = dict()
count = 1
for i in range(_input):
    name = input().strip()
    monster.setdefault(name,str(count))
    monster.setdefault(str(count),name)
    count += 1

for i in range(target):
    print(monster[input().strip()])