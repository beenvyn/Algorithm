import sys, heapq
input = sys.stdin.readline

n = int(input())

hw = []
for _ in range(n):
    d, w = map(int, input().split())
    hw.append((d,w))

hw.sort(key=lambda x:x[0])

heap = [] # 지금까지 한 과제의 점수
for d, w in hw:
    heapq.heappush(heap, w)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))