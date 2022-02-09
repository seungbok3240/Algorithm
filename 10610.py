n = list(input())

n.sort(reverse=True)

if sum([int(num) for num in n]) % 3 == 0 and '0' in n:
    print(''.join(n))
else:
    print(-1)