import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N # dp[i]: A[i]를 마지막으로 하는 증가하는 부분 수열의 최대 길이

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))