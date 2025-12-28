import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    files = list(map(int, input().split()))

    answer = 0
    heapq.heapify(files)

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        cost = a + b
        answer += cost
        heapq.heappush(files, cost)
    
    print(answer)