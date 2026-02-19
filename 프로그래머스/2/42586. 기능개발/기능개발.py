from collections import deque

def solution(progresses, speeds):
    answer = []
    que = deque()
    
    for p, s in zip(progresses, speeds):
        d = ((100 - p) + s - 1) // s
        que.append(d)
    
    while que:
        d = que.popleft()
        cnt = 1
        
        while que and d >= que[0]:
            que.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer