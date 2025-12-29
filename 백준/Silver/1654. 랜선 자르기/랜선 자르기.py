import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

# 랜선의 길이
left, right = 1, max(lines)
answer = 0

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for line in lines:
        cnt += line // mid
        if cnt > n: # 가지치기
            break
    
    if cnt >= n: # 필요한 랜선의 개수 충족 -> 랜선의 최대 길이를 구하기 위해 더 늘려보기
        answer = mid
        left = mid + 1
    else: # 랜선의 개수 부족 -> 랜선의 길이 줄이기
        right = mid - 1

print(answer)