import sys

input = sys.stdin.readline

n = int(input())
words = [list(input().rstrip()) for _ in range(n)]

importance = [0] * 26

for word in words:
    i = len(word) - 1
    for char in word:
        importance[ord(char) - ord('A')] += pow(10, i)
        i -= 1

importance.sort(reverse=True)
answer = 0
for i in range(9, -1, -1):
    answer += i * importance[9 - i]

print(answer)
