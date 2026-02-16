import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

best = float('inf') # 특성값
ans_l, ans_r = 0, 0
l, r = 0, N - 1

while l < r:
    s = arr[l] + arr[r]
    temp = abs(s)

    if temp < best:
        best = temp
        ans_l, ans_r = arr[l], arr[r]
        if best == 0:
            break
    
    if s < 0:
        l += 1
    else:
        r -= 1

print(ans_l, ans_r)