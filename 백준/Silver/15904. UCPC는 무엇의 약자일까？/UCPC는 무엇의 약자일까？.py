import sys

input = sys.stdin.readline
string = input().strip()

find = 'UCPC'
idx = 0

for char in string:
    if char == find[idx]:
        idx += 1
        if idx == 4:
            print('I love UCPC')
            break
else:
    print('I hate UCPC')