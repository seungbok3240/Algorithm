"""
https://programmers.co.kr/learn/courses/30/lessons/42883
"""


def solution(number, k):
    stack = []
    for n in number:
        if not stack:
            stack.append(n)
            continue
        if k > 0:
            while stack[-1] < n:
                stack.pop()
                k -= 1
                if not stack or k == 0:
                    break
        stack.append(n)
    if k > 0:
        answer = ''.join(stack[:-k])
    else:
        answer = ''.join(stack)
    return answer


print(solution("654321", 1))