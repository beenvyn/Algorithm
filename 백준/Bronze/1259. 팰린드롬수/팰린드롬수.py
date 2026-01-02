import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()

    if num == '0':
        break
    
    left, right = 0, len(num) - 1
    while left <= right:
        if num[left] != num[right]:
            print('no')
            break
        left += 1
        right -= 1
    else:
        print('yes')