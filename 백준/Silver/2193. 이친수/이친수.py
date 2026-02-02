import sys
input = sys.stdin.readline

n = int(input())

# dp[i][o]: 길이가 i일 때 1이 연속으로 o번인 경우의 수
dp = [[0, 0] for _ in range(n + 1)]
dp[1][1] = 1 # 길이 1에서 가능한 이친수는 "1" 하나뿐

for length in range(n):
    for one in range(2):
        cur = dp[length][one]

        # 다음 수가 0인 경우
        dp[length + 1][0] += cur
        
        # 다음 수가 1인 경우
        if one < 1:
            dp[length + 1][one + 1] += cur

print(sum(dp[n]))