"""
https://programmers.co.kr/learn/courses/30/lessons/42842
"""


def solution(brown, yellow):
    n_row = 1
    while True:
        n_col = yellow // n_row
        if n_col * n_row == yellow:
            tmp = ((n_row + 2) * 2) + (2 * (n_col))
            if tmp == brown:
                r_col, r_row = n_col + 2, n_row + 2
                if r_col <= r_row:
                    return [r_row, r_col]
        n_row += 1

    return 0