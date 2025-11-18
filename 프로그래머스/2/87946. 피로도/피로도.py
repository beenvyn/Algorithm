def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(cur_f, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and cur_f >= dungeons[i][0]:
                visited[i] = True
                dfs(cur_f - dungeons[i][1], cnt + 1)
                visited[i] = False
    
    dfs(k, 0)
    return answer