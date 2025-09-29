import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1] * n

for i, v in enumerate(arr):
    while stack and arr[stack[-1]] < v:
        answer[stack.pop()] = v
    stack.append(i)

print(*answer)