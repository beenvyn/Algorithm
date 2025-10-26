import sys
import heapq

input = sys.stdin.readline

N = int(input())
times = [list(map(int,input().split()))[1:] for _ in range(N)]
times.sort()

answer = 0
heap = []
for start, end in times:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    
    heapq.heappush(heap,end)
    answer = max(answer, len(heap))

print(answer)