import time


# # 재귀함수
# def d(n):
#     tmp = [int(x) for x in str(n)]
#     return n + sum(tmp)
#
#
# def make_list(n):
#     if n > 10000:
#         return
#     notSelfNumber = d(n)
#     if notSelfNumber > 10000:
#         return
#     if not flag[notSelfNumber]:
#         flag[notSelfNumber] = True
#         make_list(notSelfNumber)
#
#
# start_time = time.time()
# flag = [False] * 10001
# for i in range(1, 10000):
#     make_list(i)
#
# for i in range(1, 10000):
#     if not flag[i]:
#         print(i)
#
# end_time = time.time()
# print(end_time - start_time)

# 반복문
def d(n):
    tmp = [int(x) for x in str(n)]
    return n + sum(tmp)


start_time = time.time()
flag = [False] * 10001
for i in range(1, 10000):
    tmp = d(i)
    if tmp > 10000:
        continue
    flag[tmp] = True

for i in range(1, 10000):
    if not flag[i]:
        print(i)

end_time = time.time()
print(end_time - start_time)