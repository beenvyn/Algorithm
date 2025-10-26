import sys
import heapq

input = sys.stdin.readline

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()
seat_use = [0] * (N + 1)  # 좌석별 사용 횟수(1번부터)
seat_cnt = 0       # 생성된 좌석 개수

using = [] # 진행 중인 자리 (끝나는 시각, 죄석 번호)
free_seats = [] # 현재 비어 있는 좌석 번호들 -> 지금 비어 있는 좌석들 중에서 ‘번호가 가장 작은 것'을 뽑기 위해 필요
idx = 0
for start, end in times:
    while using and using[0][0] <= start:
        _, seat = heapq.heappop(using)
        heapq.heappush(free_seats, seat)

    # 배정: 가장 작은 번호의 빈 좌석이 있으면 그 좌석, 없으면 새 좌석 생성   
    if free_seats:
        seat = heapq.heappop(free_seats)
    else:
        seat_cnt += 1
        seat = seat_cnt
    
    seat_use[seat] += 1
    heapq.heappush(using, (end,seat))

print(seat_cnt)
print(*seat_use[1:seat_cnt+1])
