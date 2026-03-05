import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
l, r = 0, max(heights)

while l <= r:
    mid = (l + r) // 2 # 절단 높이
    total = 0
    for h in heights:
        if h > mid:
            total += h - mid
            if total >= M: # 목표량 채우면 더 안해도 됨 
                break
    
    if total >= M:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1
    
print(answer)