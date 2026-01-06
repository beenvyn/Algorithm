import sys
input = sys.stdin.readline

S = input().rstrip()

n = len(S)
# dp[l][r] = S[l..r] 구간에서 만들 수 있는 팰린드롬 부분수열 개수(공집합 제외)
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1 # 길이가 1인 문자들은 팰린드롬 최대 1개씩만 나옴

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1

        if S[l] != S[r]:
            # 양 끝 문자가 다르면 왼쪽 문자를 제외한 경우, 오른쪽 문자를 제외한 경우를 더해주고
            # 두 경우에 모두 포함되는 중복 영역을 제거해줌
            dp[l][r] = dp[l+1][r] + dp[l][r-1] - dp[l+1][r-1]
        else:
            # 양 끝 문자가 같으면 이 두 문자 사이의 모든 팰린드롬 부분수열을 이 두 문자로 감싸면 새로운 팰린드롬이 됨
            # 공집합을 감싸서 생기는 것도 하나의 팰린드롬이니까 +1을 해줌
            dp[l][r] = dp[l+1][r] + dp[l][r-1] + 1

print(dp[0][n-1])