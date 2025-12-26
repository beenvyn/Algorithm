import heapq

def solution(jobs):
    jobs.sort() # 요청 시각 오름차순 정렬
    n = len(jobs)
    
    idx = 0 # 아직 힙에 안넣은 jobs의 인덱스
    t = 0 # 현재 시각
    heap = [] # (소요시간, 요청시간)
    done = 0 # 처리한 작업 개수
    answer = 0
    
    while done < n:
        # 현재 시각 t까지 도착한 작업을 전부 힙에 넣기
        while idx < n and jobs[idx][0] <= t:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if heap:
            current = heapq.heappop(heap)
            t += current[0]
            answer += (t - current[1])
            done += 1
        else:
            # 아직 도착한 작업이 없다면, 다음 작업의 요청시각으로 점프
            t = jobs[idx][0]
    
    return answer // n