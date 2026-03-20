import heapq

def solution(players, m, k):
    answer = 0
    heap = [] # 현재 돌아가고 있는 서버의 증설 시간
    
    for t in range(len(players)):
        n = players[t] // m # 필요한 서버 수
        
        while heap and heap[0] + k == t: # 만료된 서버 없애기
            heapq.heappop(heap)
        
        if len(heap) < n: # 현재 돌아가고 있는 서버 수가 필요한 서버 수 보다 적으면
            for _ in range(n - len(heap)): # 필요한 만큼 서버 새로 증설
                heapq.heappush(heap, t)
                answer += 1
    
    return answer