from collections import defaultdict

n = list(input())
int_dict = defaultdict(int)

for i in n:
    if i == '6' or i == '9':
        int_dict['6'] += 1
    else:
        int_dict[i] += 1

if int_dict['6'] % 2 == 0:
    int_dict['6'] = int_dict['6'] // 2
else:
    int_dict['6'] = int_dict['6'] // 2 + 1

print(max(int_dict.values()))