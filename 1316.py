# n = int(input())
#
# cnt = 0
# for _ in range(n):
#     word = list(input())
#
#     flag = True
#     alpha = [False] * 26
#     for i in range(len(word) - 1):  # 첫 문자부터 마지막에서 두 번째 문자까지
#         if alpha[ord(word[i]) - ord('a')]:
#             flag = False
#         if word[i] == word[i + 1]:
#             continue
#         alpha[ord(word[i]) - ord('a')] = True
#
#     if alpha[ord(word[-1]) - ord('a')]:  # 마지막 문자
#         flag = False
#
#     if flag:
#         cnt += 1
#
# print(cnt)

n = int(input())

cnt = n
for _ in range(n):
    word = list(input())

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            continue

        if word[i] in word[(i + 1):]:
            cnt -= 1
            break

print(cnt)
