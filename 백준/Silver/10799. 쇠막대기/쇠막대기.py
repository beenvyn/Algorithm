brackets = input()
stack = []
answer = 0

for i in range(len(brackets)):
    if brackets[i] == ')':
        if brackets[i- 1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
        continue
    stack.append(brackets[i])

print(answer)