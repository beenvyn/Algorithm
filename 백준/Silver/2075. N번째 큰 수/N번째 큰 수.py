import sys
import heapq
input = sys.stdin.readline

N = int(input())

# 큰 수 N개만 남기기
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(N - 1):
    row = list(map(int, input().split()))

    for i in range(N):
        heapq.heappush(heap, row[i])

        # 힙 크기를 N으로 유지
        while len(heap) > N:
            heapq.heappop(heap)

print(heap[0])