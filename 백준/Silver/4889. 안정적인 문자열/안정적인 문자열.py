num = 0
while True:
    string = input()
    num += 1
    if '-' in string:
        break

    stack = []
    answer = 0
    
    for s in string:
        if not stack and s == '}':
            answer += 1
            stack.append('{')
        elif stack and s == '}':
            stack.pop()
        else:
            stack.append(s)
    answer += len(stack) // 2
        
    print(f'{num}. {answer}')