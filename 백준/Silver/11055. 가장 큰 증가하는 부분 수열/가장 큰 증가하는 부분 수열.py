import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# dp[i]: A[i]로 끝나는 부분 수열 중 가장 합이 큰 증가하는 부분 수열의 합
dp = [0] * N
dp[0] = A[0]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]) 
    dp[i] += A[i]

print(max(dp))