from collections import deque

def solution(N, road, K):
    answer = 0
    infos = [[] for _ in range(N + 1)]
    
    for a, b, t in road:
        infos[a].append([b, t])
        infos[b].append([a, t])
    
    time = [float('inf')] * (N + 1)
    time[1] = 0
    
    que = deque([(0, 1)]) # 시간, 노트
    
    while que:
        cur_t, v = que.popleft()
        
        if cur_t > time[v]:
            continue
        
        for u, t in infos[v]:
            next_t = cur_t + t
            if next_t < time[u]:
                time[u] = next_t
                que.append((next_t, u))
    
    for t in time:
        if t <= K:
            answer += 1
    return answer