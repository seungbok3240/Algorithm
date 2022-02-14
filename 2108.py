from collections import Counter
import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

# 산술평균
print(round(sum(numbers) / n))

# 중앙값
numbers.sort()
print(numbers[n // 2])

# 최빈값
if n == 1:
    print(numbers[0])
else:
    cnt = Counter(numbers)
    cnt_tmp = cnt.most_common(2)
    if cnt_tmp[0][1] == cnt_tmp[1][1]:
        print(cnt_tmp[1][0])
    else:
        print(cnt_tmp[0][0])


# 범위
print(numbers[-1] - numbers[0])