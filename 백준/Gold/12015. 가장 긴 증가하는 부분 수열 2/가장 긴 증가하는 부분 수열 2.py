import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 길이별 최소 끝값
# tails[i]: 길이가 i+1인 증가 수열 중 마지막 값이 가장 작은 값
tails = [nums[0]] 

for i in range(1, n):
    x = nums[i]
    if x > tails[-1]:
        tails.append(x)
    else: # 최적화 과정임. 해당 길이의 끝값을 더 작게 만들어서 이후 더 긴 수열로 확장될 가능성을 키움
        left, right = 0, len(tails) - 1
        idx = 0 # tails에서 처음으로 x 이상이 되는 자리
        while left <= right:
            mid = (left + right) // 2

            if tails[mid] < x:
                left = mid + 1
            else:
                idx = mid
                right = mid - 1
        tails[idx] = x

print(len(tails))
