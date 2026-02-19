from collections import deque

def solution(maps):
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    rows, cols = len(maps), len(maps[0])
    
    def bfs(start, end):
        visited = [[False] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if maps[r][c] == start:
                    que = deque([(r, c, 0)])
                    visited[r][c] = True
                    
        while que:
            r, c, time = que.popleft()
            
            if maps[r][c] == end:
                return time
            
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                
                if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] != 'X' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    que.append((nr, nc, time + 1))
        return -1
    
    to_lever = bfs('S', 'L')
    to_exit = bfs('L', 'E')
    
    if to_lever == -1 or to_exit == -1:
        return -1
    else:
        return to_lever + to_exit