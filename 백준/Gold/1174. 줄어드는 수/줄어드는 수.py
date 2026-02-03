import sys
input = sys.stdin.readline

N = int(input())

nums = []

def backtrack(s, idx):
    nums.append(int(s))

    for j in range(idx):
        backtrack(s + str(j), j)

for i in range(10):
    backtrack(str(i), i)

nums.sort()
print(nums[N - 1]) if N <= len(nums) else print(-1)