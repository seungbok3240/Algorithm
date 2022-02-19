# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
#
# n2 = int(input())
# a2 = list(map(int, input().split()))
#
#
# def bs(target):
#     start = 0
#     end = n - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if target == a[mid]:
#             return 1
#         elif target < a[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return 0
#
#
# for i in a2:
#     print(bs(i))


# # use set
# n = int(input())
# a = set(map(int, input().split()))
#
# n2 = int(input())
# a2 = list(map(int, input().split()))
#
# for i in a2:
#     if i in a:
#         print(1)
#     else:
#         print(0)

