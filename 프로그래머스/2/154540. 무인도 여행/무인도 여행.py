from collections import deque

def solution(maps):
    answer = []
    rows, cols = len(maps), len(maps[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False] * cols for _ in range(rows)]
    
    def bfs(i,j):
        days = 0
        days += int(maps[i][j])
        que = deque([(i,j)])
        visited[i][j] = True
        
        while que:
            r, c = que.popleft()
        
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
            
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    que.append((nr,nc))
                    days += int(maps[nr][nc])
        answer.append(days)
    
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and maps[i][j] != 'X':
                bfs(i,j)
    
    return sorted(answer) if answer else [-1]