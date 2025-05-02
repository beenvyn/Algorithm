from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    visited = [[False] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            if board[j][i] == 'R':
                sx, sy = i, j
                
    queue = deque([(sx, sy, 0)])
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if board[y][x] == 'G':
            return cnt
        
        for k in range(4):
            nx = x
            ny = y
            
            while 0 <= nx + dx[k] < m and 0 <= ny + dy[k] < n and board[ny + dy[k]][nx + dx[k]] != 'D':
                nx += dx[k]
                ny += dy[k]
                
            if not visited[ny][nx]:
                queue.append((nx, ny, cnt + 1))
                visited[ny][nx] = True  
    
    return -1