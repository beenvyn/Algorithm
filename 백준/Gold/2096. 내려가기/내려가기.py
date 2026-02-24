import sys
input = sys.stdin.readline

n = int(input())

# 맨 처음 세개의 숫자를 입력받아 DP의 초기 값 설정
nums = list(map(int, input().split()))
max_dp = nums
min_dp = nums

# 총 n번 입력 받음(위에 한 번 입력받았으니까 여기선 n-1번)
for i in range(n-1):
    # 매번 새롭게 갱신
    nums = list(map(int, input().split()))
    max_dp = [nums[0] + max(max_dp[0], max_dp[1]), nums[1] + max(max_dp), nums[2] + max(max_dp[1], max_dp[2])]
    min_dp = [nums[0] + min(min_dp[0], min_dp[1]), nums[1] + min(min_dp), nums[2] + min(min_dp[1], min_dp[2])]

print(max(max_dp), min(min_dp))