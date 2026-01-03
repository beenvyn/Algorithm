import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# dp[l][r]: 구간 l~r을 팰린드롬으로 만들기 위해 필요한 최소 삽입 개수
dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1

        # 양 끝 값이 같다면 이미 팰린드롬의 양쪽이 맞아 있음
        # → 안쪽 구간(l+1 ~ r-1)만 해결하면 됨
        if nums[l] == nums[r]:
            dp[l][r] = dp[l+1][r-1]
        # 양 끝 값이 다르다면 둘 중 하나는 반드시 짝을 만들어야 함
        # 1) arr[l]을 오른쪽에 하나 삽입 → 구간(l+1 ~ r)만 해결하면 됨
        # 2) arr[r]을 왼쪽에 하나 삽입 → 구간(l ~ r-1)만 해결하면 됨
        # 둘 중 더 적게 드는 쪽 선택 + 삽입 1회
        else:
            dp[l][r] = min(dp[l+1][r], dp[l][r-1]) + 1

print(dp[0][n-1])