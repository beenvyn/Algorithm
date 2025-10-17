import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = list(map(int, input().split()))
ops = ['+', '-', '*', '/']

def apply(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    else:
        if x < 0 and y != 0:
            return -((-x) // y)
        return x // y

answer = []
def backtrack(cur, idx):
    if idx == n:
        answer.append(cur)
        return

    for i in range(4):
        if cnt[i] <= 0:
            continue
        cnt[i] -= 1
        backtrack(apply(cur,nums[idx],ops[i]), idx+1)
        cnt[i] += 1

backtrack(nums[0], 1)

print(max(answer))
print(min(answer))
