import sys
input = sys.stdin.readline

S = input().rstrip()
S += ' '

answer = ''
stack = []
bracket = False

for ch in S:
    if ch == '<': # < 이전에 오는 것들은 뒤집어야 함
        bracket = True
        while stack:
            answer += stack.pop()
    stack.append(ch)

    if ch == '>': # > 이전에 오는 것들은 그대로 둬야 함
        bracket = False
        while stack:
            answer += stack.pop(0)

    if ch == ' ' and not bracket: # 괄호 밖 공백 이전에 오는 것들은 뒤집어야 함
        stack.pop()
        while stack:
            answer += stack.pop()
        answer += ' '

print(answer)