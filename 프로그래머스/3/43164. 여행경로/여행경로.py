def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [False] * n # 도시가 아니라 항공권을 관리
    tickets.sort() # 알파벳 순 보장
    
    def dfs(cur, path):
        if len(path) == n + 1: # 첫 번째 정답만 찾고 바로 종료
            answer.extend(path)
            return True
        
        for i in range(n):
            start, end = tickets[i]
            
            if not visited[i] and start == cur:
                visited[i] = True
                
                if dfs(end, path + [end]):
                    return True
                
                visited[i] = False
        
        return False
    
    dfs("ICN", ["ICN"])
    
    return answer