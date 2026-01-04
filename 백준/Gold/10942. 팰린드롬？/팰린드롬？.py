import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]
answers = []

# dp[l][r]: 구간 l~r이 팰린드롬인지
dp = [[1] * N for _ in range(N)]

for length in range(2, N + 1):
    for l in range(N - length + 1):
        r = l + length - 1
        # l, r이 같고 dp[l-1][r-1]이 팰린드롬이면 참
        if nums[l] == nums[r] and dp[l+1][r-1]: 
            dp[l][r] = 1
        else:
            dp[l][r] = 0

for q in questions:
    l, r = q
    answers.append(dp[l-1][r-1])

for ans in answers:
    print(ans)