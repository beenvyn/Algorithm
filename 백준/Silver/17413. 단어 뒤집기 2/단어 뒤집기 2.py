data = input() + ' '
stack = []
answer = ''
tag = False # 괄호 안에 있는지 여부

for d in data:
    if d == '<':
        tag = True # 괄호 안에 있음 표시
        for _ in range(len(stack)): # 괄호 만나기 이전 스택 안에 있는 것들을
            answer += stack.pop() # 뒤집어서 더해주기
    stack.append(d)

    if d == '>':
        tag = False # 괄호 빠져 나왔음 표시
        for _ in range(len(stack)): # 괄호 안에 있는 것들은
            answer += stack.pop(0) # 그대로 더해주기
    
    if tag == False and d == ' ': # 괄호 밖 공백을 만나면
        stack.pop() # 들어간 공백을 빼주고
        for _ in range(len(stack)): # 뒤집어서 더하기
            answer += stack.pop()
        answer += ' ' # 마지막에 공백 살려주기

print(answer)