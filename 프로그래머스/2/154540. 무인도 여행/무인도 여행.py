from collections import deque

def solution(maps):
    answer = []
    col = len(maps)
    row = len(maps[0])
    visited = [[False] * row for _ in range(col)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(col):
        for j in range(row):
            if maps[i][j] != 'X' and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                total = int(maps[i][j])
    
                while queue:
                    y, x = queue.popleft()
        
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
            
                        if 0 <= ny < col and 0 <= nx < row:
                            if maps[ny][nx] != 'X' and not visited[ny][nx]:
                                queue.append((ny, nx))
                                visited[ny][nx] = True
                                total += int(maps[ny][nx])
        
                answer.append(total)
    
    answer.sort()
    return answer or [-1]