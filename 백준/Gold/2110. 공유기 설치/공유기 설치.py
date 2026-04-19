import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

houses.sort()

# 이 거리를 유지하면서 C개 이상의 공유기를 설치할 수 있는지 확인
def can_install(dist):
    # 첫 번째 집에는 무조건 설치
    count = 1
    last = houses[0]

    # 이전에 설치한 집과의 거리가 dist 이상이면 설치
    for i in range(1, N):
        if houses[i] - last >= dist:
            count += 1
            last = houses[i]
    
    if count >= C:
        return True
    else:
        return False

# 공유기 사이의 "최소 거리"를 기준으로 이분 탐색
l = 1 # 가능한 최소 거리
r = houses[-1] - houses[0] # 가능한 최대 거리

answer = 0

while l <= r:
    mid = (l + r) // 2

    if can_install(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)