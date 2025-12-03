import sys, heapq
input = sys.stdin.readline

n = int(input())

dates = []
for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    dates.append((m1, d1, m2, d2))

days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def date_to_days(month, day):
    days = 0
    for i in range(1, month):
        days += days_per_month[i]
    return days + day

flowers = []
for m1, d1, m2, d2 in dates:
    start = date_to_days(m1, d1)
    end = date_to_days(m2, d2)
    flowers.append((start, end))

flowers.sort(key=lambda x:x[0])

start_day = date_to_days(3,1)
end_day = date_to_days(11,30)

idx = 0 # 지금 보고 있는 꽃
heap = [] # 지금까지 선택한 꽃의 지는 날짜
count = 0

while start_day <= end_day:
    while idx < n and flowers[idx][0] <= start_day:
        heapq.heappush(heap, -flowers[idx][1])
        idx += 1
    
    if heap:
        count += 1
        start_day = -heapq.heappop(heap)
    else:
        print(0)
        break
else:
    print(count)