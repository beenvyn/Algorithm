import sys, heapq
input = sys.stdin.readline

n = int(input())

stations = []
for _ in range(n):
    dist, fuel = map(int, input().split())
    stations.append((dist, fuel))
l, p = map(int, input().split())

stations.sort(key=lambda x:x[0])

count = 0
max_dist = p # 현재 도달 가능한 최대 거리
idx = 0 # stations에서 어디까지 봤는지
heap = [] # 지금까지 갈 수 있는 주유소들의 연료량

while max_dist < l:
    # 현재 연료로 도달 가능한 모든 주유소를 힙에 넣기
    while idx < n and stations[idx][0] <= max_dist:
        heapq.heappush(heap, -stations[idx][1])
        idx += 1
    
    # 힙에서 가장 연료가 많은 주유소를 골라서 주유
    if heap:
        max_dist += -heapq.heappop(heap)
        count += 1
    else: # 더 이상 갈 수 있는 주유소가 없는데 목적지에 못 갔으면 실패
        print(-1)
        break
else:
    print(count)