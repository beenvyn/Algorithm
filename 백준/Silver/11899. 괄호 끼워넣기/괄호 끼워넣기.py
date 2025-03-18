s = input()

stack = []
answer = 0

for c in s:
    if c == '(':
        stack.append('(')
    else:
        if stack:
            stack.pop()
        else:
            answer += 1

print(len(stack) + answer)
        