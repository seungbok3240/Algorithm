"""
https://programmers.co.kr/learn/courses/30/lessons/77885
"""


def solution(numbers):
    answer = []

    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bi = list('0' + bin(number)[2:])
            idx = ''.join(bi).rfind('0')

            bi[idx] = '1'
            bi[idx + 1] = '0'

            answer.append(int(''.join(bi), 2))

    return answer