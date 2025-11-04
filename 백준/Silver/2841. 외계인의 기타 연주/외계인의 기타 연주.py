import sys

input = sys.stdin.readline

N, P = map(int, input().split())
notes = [list(map(int, input().split())) for _ in range(N)]

stacks = [[] for _ in range(7)] # 더 작은 수를 만나지 않은 음
answer = 0

for i in range(N):
    m, f = notes[i]
    stack = stacks[m]
    
    while stack and stack[-1] > f:
        stack.pop()
        answer += 1
    
    if stack and stack[-1] == f:
        continue

    stack.append(f) 
    answer += 1  

print(answer)