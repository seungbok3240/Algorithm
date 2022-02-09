import re

text = input()
n = re.split('([+ | -])', text)

fixed_n = list()
fixed_n.append(str(int(n[0])))
i = 1
while i < len(n):
    if n[i] == '-':
        fixed_n.append(n[i])
        i += 1

    elif n[i] == '+':
        tmp = int(fixed_n[-1]) + int(n[i + 1])
        fixed_n.pop()
        fixed_n.append(str(tmp))
        i += 2
    else:
        tmp = str(int(n[i]))
        fixed_n.append(tmp)
        i += 1

print(eval(''.join(fixed_n)))

a = input().split('-')

# 다른 사람 코드

# ans = 0
# for i in range(len(a)):
#     if i == 0:
#         ans += sum(list(map(int,a[i].split('+'))))
#
#     else :
#        ans -= sum(list(map(int,a[i].split('+'))))
#
#
# print(ans)

