import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = input().rstrip()

stack = []

for ch in num:
    while K > 0 and stack and stack[-1] < ch:
        stack.pop()
        K -= 1

    stack.append(ch)

if K > 0:
    stack = stack[:-K]

print(''.join(stack))