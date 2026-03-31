from collections import deque

def solution(storage, requests):
    rows, cols = len(storage), len(storage[0])
    
    board = [['.'] * (cols + 2) for _ in range(rows + 2)]
    for r in range(rows):
        for c in range(cols):
            board[r + 1][c + 1] = storage[r][c]
    
    rows += 2
    cols += 2
    
    def crane(req):
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == req[0]:
                    board[r][c] = '.'
                    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 외부랑 연결된 빈 공간의 좌표 찾기
    def get_outside():
        visited = [[False] * cols for _ in range(rows)]
        
        que = deque([(0, 0)])
        visited[0][0] = True
        
        while que:
            r, c = que.popleft()
            
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] == '.':
                    visited[nr][nc] = True
                    que.append((nr, nc))
                    
        # visited=True인 '.'들이 외부와 연결된 공간
        return visited
    

    def forklift(req):
        outside = get_outside()
        remove = []
        
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == req:
                    # 상하좌우 중 하나라도 외부 공간이면 제거 가능
                    for d in dirs:
                        nr, nc = r + d[0], c + d[1]
                        
                        if outside[nr][nc]:
                            remove.append((r, c))
                            break
        
        # 동시에 제거
        for r, c in remove:
            board[r][c] = '.'
        
    for req in requests:
        if len(req) == 2:
            crane(req)
        else:
            forklift(req)
    
    answer = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if board[r][c] != '.':
                answer += 1
    
    return answer