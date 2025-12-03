import sys, heapq
input = sys.stdin.readline

n = int(input())

infos = []
for _ in range(n):
    p, d = map(int, input().split())
    infos.append((d, p))

infos.sort(key=lambda x:x[0])

heap = [] # 지금까지 선택한 강연들의 강연료 저장

for d, p in infos:
    # 일단 이 강연을 선택해본다
    heapq.heappush(heap, p)

    # 마감일 d일까지는 최대 d개의 강연만 할 수 있음
    # 만약 지금까지 선택한 강연 수가 마감일 d를 초과하면
    # => 가장 싼 강연을 하나 버린다
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))