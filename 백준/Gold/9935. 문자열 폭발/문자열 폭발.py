import sys
input = sys.stdin.readline

S = input().rstrip()
word = input().rstrip()

stack = []
n = len(word)

for ch in S:
    stack.append(ch)

    if len(stack) >= n and stack[-n:] == list(word):
        for _ in range(n):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')