from collections import deque

def solution(maps):
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    
    q = deque([(0,0,1)])
    visited[0][0] = True
    
    while q:
        r, c, dist = q.popleft()
        
        if r == row - 1 and c == col - 1:
            return dist
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] != 0 and not visited[nr][nc]:
                q.append((nr,nc,dist+1))
                visited[nr][nc] = True

    return -1