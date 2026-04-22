import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    for w in works:
        heapq.heappush(heap, -w)
    
    for _ in range(n):
        if heap:
            x = -heapq.heappop(heap)
            x -= 1
            if x > 0:
                heapq.heappush(heap, -x)
    
    while heap:
        x = heapq.heappop(heap)
        answer += x**2
    
    return answer