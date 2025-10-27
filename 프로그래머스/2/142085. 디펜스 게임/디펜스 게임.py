import heapq

def solution(n, k, enemy):
    heap = []
    for i, e in enumerate(enemy):
        heapq.heappush(heap,-e)
        n -= e
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return i
    return len(enemy)