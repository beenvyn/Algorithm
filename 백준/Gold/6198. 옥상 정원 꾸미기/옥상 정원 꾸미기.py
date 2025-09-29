import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input().strip()) for _ in range(n)]
stack = []
answer = [0] * n
cnt = 0

for i in range(n):
    while stack and arr[stack[-1]] <= arr[i]:
        answer[stack.pop()] = i
    stack.append(i)

for i, v in enumerate(answer):
    if v == 0:
        cnt += n - i - 1
    else:
        cnt += v - i - 1

print(cnt)
