import heapq

def solution(n, k, enemy):
    # 적 수를 계속 저장
    # 병사 먼저 깎는다
    # 병사가 부족하면 지금까지 중 가장 큰 적을 무적권으로 되돌리기

    heap = [] # 물리친 적 수 저장(최대 힙)
    
    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e) # 일단 병사로 막음
        n -= e
        
        if n < 0: # 병사가 부족하면 무적권으로 되돌리기
            if k > 0:
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return i
            
    # 전부 물리친 경우
    return len(enemy)