from collections import deque

def solution(x, y, n):
    answer = 0
    visited = [False] * (y + 1)

    que = deque([(x, 0)])
    
    while que:
        cur_x, cnt = que.popleft()
        
        if cur_x == y:
            return cnt
        
        for nxt in [cur_x + n, cur_x * 2, cur_x * 3]:
            if nxt <= y and not visited[nxt]:
                visited[nxt] = True
                que.append((nxt, cnt + 1))
    
    return -1