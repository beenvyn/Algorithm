from collections import deque

def solution(players, m, k):
    answer = 0
    que = deque([]) # 서버 만료 시간
    
    for time, player in enumerate(players):
        while que and que[0] == time:
            que.popleft()
        
        needed_server, current_server = player // m, len(que)
        if needed_server > current_server:
            for _ in range(needed_server - current_server):
                que.append(time + k)
                answer += 1
            
    return answer