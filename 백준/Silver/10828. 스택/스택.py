import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    inst = input().split()

    if inst[0] == 'push':
        stack.append(inst[1])
    elif inst[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif inst[0] == 'size':
        print(len(stack))
    elif inst[0] == 'empty':
        x = 0 if stack else 1
        print(x)
    elif inst[0] == 'top':
        x = stack[-1] if stack else -1
        print(x)

