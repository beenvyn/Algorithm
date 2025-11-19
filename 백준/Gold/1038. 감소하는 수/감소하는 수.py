import sys
input = sys.stdin.readline

N = int(input())
nums = []

def dfs(last_digit, cur_num):
    nums.append(cur_num)

    for next_digit in range(0, last_digit):
        dfs(next_digit, cur_num * 10 + next_digit)

for n in range(10):
    dfs(n,n)

nums.sort()
if N < len(nums):
    print(nums[N])
else:
    print(-1)