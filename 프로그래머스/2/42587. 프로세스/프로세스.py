from collections import deque

def solution(priorities, location):
    n = len(priorities)
    answer = [0] * n
    order = 1
    
    que = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    
    while que:
        idx, priority = que.popleft()
        
        flag = True # 현재 프로세스가 가장 높은 우선순위인지 여부
        for i, p in que:
            if p > priority:
                que.append((idx, priority))
                flag = False
                break
        
        if flag:
            answer[idx] = order
            order += 1
        
    return answer[location]