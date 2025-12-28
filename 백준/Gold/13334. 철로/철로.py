import sys, heapq
input = sys.stdin.readline

n = int(input())

coords = []
for _ in range(n):
    coord = list(map(int, input().split()))
    coord.sort()
    coords.append(coord)

d = int(input())

coords.sort(key=lambda x:x[1]) # r 오름차순

answer = 0
heap = [] # l들을 담는 힙

for l, r in coords:
    R = r # 오른쪽 끝을 고정해서 생각하기
    heapq.heappush(heap, l) # 일단 현재 구간의 l을 후보로 넣는다

    # 철로 왼쪽 경계는 R - d, 그보다 작은 l은 제거
    while heap and heap[0] < R - d:
        heapq.heappop(heap)

    answer = max(answer, len(heap))

print(answer)