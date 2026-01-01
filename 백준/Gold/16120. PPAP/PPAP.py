import sys
input = sys.stdin.readline

string = input().rstrip()

# 반대로 생각해서 이미 만들어진 문자열에서 PPAP를 P로 변환
stack = []
for ch in string:
    stack.append(ch)

    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(4):
            stack.pop()
        stack.append('P')

if stack == ['P']:
    print('PPAP')
else:
    print('NP')