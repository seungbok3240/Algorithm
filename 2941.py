# alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# n = input()
#
# cnt = 0
#
# for a in alpha:
#     while a in n:
#         n = n.replace(a, ' ', 1)
#         cnt += 1
#
# tmp = n.split()
# tmp = ''.join(tmp)
# cnt += len(tmp)
# print(cnt)

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()

for a in alpha:
    n = n.replace(a, 'A')

print(len(n))