import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000

# dp[i][l][a] = i일째까지 왔을 때 (지각 l번, 연속결석 a번)인 경우의 수
dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1 # 아무 출결도 없는 상태는 1가지

# i일째 상태에서 다음 날 출결을 붙인다
for day in range(N):
    for late in range(2):
        for absent in range(3):
            cur = dp[day][late][absent]

            # 출석
            dp[day + 1][late][0] = (dp[day + 1][late][0] + cur) % MOD

            # 지각
            if late == 0:
                dp[day + 1][1][0] = (dp[day + 1][1][0] + cur) % MOD

            # 결석
            if absent < 2:
                dp[day + 1][late][absent + 1] = (dp[day + 1][late][absent + 1] + cur) % MOD 

answer = 0
for late in range(2):
    for absent in range(3):
        answer = (answer + dp[N][late][absent]) % MOD

print(answer)