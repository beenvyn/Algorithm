import sys
import heapq

input = sys.stdin.readline

N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]
times.sort()

heap = []
answer = 0
for start, end in times:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap,end)
    answer = max(answer,len(heap))

print(answer)