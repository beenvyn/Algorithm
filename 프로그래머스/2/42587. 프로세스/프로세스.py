from collections import deque

def solution(priorities, location):
    cnt = 0
    
    # [(2,0), (1,1), (3,2), (2,3)]
    que = deque([(p, idx) for idx, p in enumerate(priorities)])
    
    while que:
        cur_p, cur_idx = que.popleft()
        flag = True
        
        for p, idx in que:
            if p > cur_p:
                que.append((cur_p, cur_idx))
                flag = False
                break
        
        if flag:
            cnt += 1
            if cur_idx == location:
                return cnt
