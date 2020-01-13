import itertools

a, b = map(int, input().split())

table = []

for i in range(a):
    table.append(str(i+1))

p_list = list(map(' '.join, itertools.permutations(table,b)))

for i in p_list:
    print(i)