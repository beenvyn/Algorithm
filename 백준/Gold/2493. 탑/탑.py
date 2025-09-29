import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_reversed = arr[::-1]
stack = []
answer = [0] * n

for i in range(n):
    while stack and arr_reversed[stack[-1]] <= arr_reversed[i]:
        answer[stack.pop()] = n - i

    stack.append(i)

print(*answer[::-1])