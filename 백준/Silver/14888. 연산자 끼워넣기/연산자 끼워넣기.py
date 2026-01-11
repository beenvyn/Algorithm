import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
opts = list(map(int, input().split())) # +, - , *, /

min_answer = float('inf')
max_answer = -float('inf')

# 다음에 사용할 숫자 인덱스, 현재 계산된 값
def dfs(idx, val):
    global min_answer, max_answer
    if idx == N:
        min_answer = min(min_answer, val)
        max_answer = max(max_answer, val)
        return

    for i in range(4):
        next_val = 0
        if opts[i] > 0:
            if i == 0:
                next_val = val + nums[idx]
            elif i == 1:
                next_val = val - nums[idx]
            elif i == 2:
                next_val = val * nums[idx]
            else:
                next_val = int(val / nums[idx])
            opts[i] -= 1
            dfs(idx + 1, next_val)
            opts[i] += 1
                
dfs(1, nums[0])
print(max_answer)
print(min_answer)