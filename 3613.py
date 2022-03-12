import sys
import re

s = sys.stdin.readline().rstrip()


def printError():
    print("Error!")
    sys.exit(0)


if '_' in s:
    words = re.findall('[a-z]+', s)  # c++ 대문자 유무 체크
    if s != '_'.join(words):
        printError()

    tmp = s.split('_')
    result = tmp[0]
    for i in range(1, len(tmp)):
        tmp[i] = tmp[i][0].upper() + tmp[i][1:]
        result = result + tmp[i]
    print(result)
else:
    a = re.findall('[^\w]', s)  # java 특수문자 체크
    if a:
        print('Error!')
        sys.exit(0)

    tmp = re.findall('([a-z]+)|([A-Z][a-z]*)', s)  # java 첫 문자 대소문자 판단
    if tmp[0][0] == '':
        print('Error!')
        sys.exit(0)

    result = tmp[0][0]
    for i in range(1, len(tmp)):
        if tmp[i][0] == '':
            result = result + '_' + tmp[i][1].lower()
        else:
            result = result + '_' + tmp[i][0].lower()
    print(result)
