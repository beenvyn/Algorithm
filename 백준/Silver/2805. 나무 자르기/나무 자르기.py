import sys

input = sys.stdin.readline

N, M = map(int,input().split())
heights = list(map(int,input().split()))

left, right = 0, max(heights)
answer = 0

while left <= right:
    mid = (left + right) // 2

    total = 0
    for h in heights:
        if h > mid:
            total += h - mid
            if total >= M:    # 목표량 채우면 더 안 더해도 됨
                break
    
    if total >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
