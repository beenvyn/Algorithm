import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    
    dp = [[0,0,0] for _ in range(n + 1)] # 인접한 선택이 안 되도록 DP 상태를 나눔

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i-1]) # i번째 열에서 스티커를 안떼는 경우
        dp[i][1] = stickers[0][i-1] + max(dp[i-1][2], dp[i-1][0]) # i번째 열의 첫 번째 행에 있는 스티커를 떼는 경우
        dp[i][2] = stickers[1][i-1] + max(dp[i-1][1], dp[i-1][0]) # i번째 열의 두 번째 행에 있는 스티커를 떼는 경우
    
    print(max(dp[n]))