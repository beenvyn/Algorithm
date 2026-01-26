import heapq

def solution(jobs):
    n = len(jobs)
    jobs.sort()
    
    idx = 0 # 아직 힙에 안넣은 job의 인덱스
    pq = [] # 대기큐
    cur_time = 0 # 현재 시각
    cnt = 0 # 처리한 작업 수
    total = 0 # 반환 시간의 합
    
    while cnt < n:
        while idx < n and jobs[idx][0] <= cur_time:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if pq:
            l, s = heapq.heappop(pq)
            cur_time += l
            total += (cur_time - s)
            cnt += 1
        else:
            cur_time = jobs[idx][0]
            
    return total // n