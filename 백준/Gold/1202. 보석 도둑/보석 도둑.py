import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())

infos = []
for _ in range(N):
    w, v = map(int,input().split())
    infos.append((w, v))

bags = []
for _ in range(K):
    bags.append(int(input()))

infos.sort(key=lambda x:x[0]) # 무게기준 오름차순 정렬
bags.sort()

total = 0
heap = [] # 가격을 저장하는 최대 힙
idx = 0 # 현재까지 확인한 보석 인데스

for bag in bags:
    # 이 가방이 담을 수 있는 모든 보석을 heap에 넣는다
    while idx < N and infos[idx][0] <= bag:
        # 가격을 기준으로 최대 힙을 만들기 위해 음수로 넣기
        heapq.heappush(heap, -infos[idx][1])
        idx += 1
    
    # 담을 수 있는 보석들 중 가장 비싼 것 하나 선택
    if heap:
        total += -heapq.heappop(heap)

print(total)