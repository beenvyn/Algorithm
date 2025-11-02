import heapq

def solution(scoville, K):
    cnt = 0
    
    heapq.heapify(scoville)
    
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville,a + 2*b)
        cnt += 1
    
    return cnt