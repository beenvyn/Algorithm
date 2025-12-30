import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

tails = [A[0]] # tails[i]: 길이가 i + 1인 증가 수열 중 가장 작은 마지막 값

for i in range(1, n):
    x = A[i]
    if x > tails[-1]:
        tails.append(x)
    else:
        left, right = 0, len(tails) - 1
        idx = 0 # tails에서 처음으로 x 이상이 되는 원소의 위치
    
        while left <= right:
            mid = (left + right) // 2
            if tails[mid] < x:
                left = mid + 1
            else:
                idx = mid
                right = mid - 1
        tails[idx] = x

print(len(tails))