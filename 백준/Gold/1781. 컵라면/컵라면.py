import sys, heapq
input = sys.stdin.readline

n = int(input())

qs = []
for _ in range(n):
    d, r = map(int, input().split())
    qs.append((d, r))

qs.sort(key=lambda x:x[0])

heap = [] # 지금까지 선택한 문제의 컵라면 개수

for d, r in qs:
    heapq.heappush(heap, r)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))