from collections import deque

def bfs(start, end, maps):
    col = len(maps)
    row = len(maps[0])
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    distance = [[0] * row for _ in range(col)]
    
    for i in range(col):
        for j in range(row):
            if maps[i][j] == start:
                sy, sx = i, j
            elif maps[i][j] == end:
                ey, ex = i, j
                
    queue = deque([(sy, sx)])
    
    while queue:
        y, x = queue.popleft()
                
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
        
            if 0 <= nx < row and 0 <= ny < col and not distance[ny][nx] and maps[ny][nx] != 'X':
                if nx == ex and ny == ey:
                    return distance[y][x] + 1
                distance[ny][nx] = distance[y][x] + 1
                queue.append((ny, nx))
    return -1

def solution(maps):
    to_lever = bfs('S', 'L', maps)
    to_end = bfs('L', 'E', maps)
    
    if to_lever != -1 and to_end != -1:
        return to_lever + to_end
    else:
        return -1