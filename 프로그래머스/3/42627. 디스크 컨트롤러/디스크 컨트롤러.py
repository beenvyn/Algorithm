import heapq

def solution(jobs):
    answer = 0
    now = 0 # 현재 시간
    i = 0 # 처리 개수
    start = -1 # 마지막 완료 시간
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,(job[1],job[0]))
        
        if heap:
            x = heapq.heappop(heap)
            start = now
            now += x[0]
            answer += now - x[1]
            i += 1
        else:
            now += 1
    
    return answer // len(jobs)