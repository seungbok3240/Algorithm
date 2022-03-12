import sys

code = sys.stdin.read()

while 'BUG' in code:
    code = code.replace('BUG', '')
print(code)