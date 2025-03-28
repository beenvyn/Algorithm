nums = input()
n = 0
idx = 0

while True:
    n += 1
    for s in str(n): # 두 자리수 이상일 경우 n의 모든 자리수를 비교해야 함
        if s == nums[idx]:
            idx += 1
            if idx >= len(nums):
                print(n)
                exit()