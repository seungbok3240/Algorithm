"""
https://programmers.co.kr/learn/courses/30/lessons/87946
"""


from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        now_fatigue = k
        cnt = 0
        for d in p:
            if now_fatigue >= d[0]:
                now_fatigue -= d[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))