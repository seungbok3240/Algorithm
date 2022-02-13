from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    paper_list = deque([(int(number), index) for index, number in enumerate(importance)])
    target = paper_list[m]
    cnt = 0
    while True:
        if paper_list[0] == max(paper_list, key=lambda item:item[0]):
            tmp = paper_list.popleft()
            cnt += 1
            if target == tmp:
                print(cnt)
                break
        else:
            paper_list.rotate(-1)

# from collections import deque
#
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     importance = deque(list(map(int, input().split())))
#     index = deque([i for i in range(n)])
#     target_importance = importance[m]
#     target_index = index[m]
#     cnt = 0
#     while True:
#         if importance[0] == max(importance):
#             tmp_importance = importance.popleft()
#             tmp_index = index.popleft()
#             cnt += 1
#             if target_importance == tmp_importance and target_index == tmp_index:
#                 print(cnt)
#                 break
#         else:
#             importance.rotate(-1)
#             index.rotate(-1)