from collections import deque

def solution(places):
    answer = []
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    def check(r, c, place):
        visited = [[False] * 5 for _ in range(5)]
        
        que = deque([(r, c, 0)])
        visited[r][c] = True
        
        while que:
            r, c, dist = que.popleft()
            
            if dist == 2:
                continue
                
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                
                if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                    if place[nr][nc] == 'P':
                        return False
                    
                    if place[nr][nc] == 'X':
                        continue
                    
                    que.append((nr, nc, dist + 1))
                    visited[nr][nc] = True
        return True 
    
    for place in places:
        ok = True
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    if not check(r, c, place):
                        ok = False
                        break
        answer.append(1 if ok else 0)
    return answer