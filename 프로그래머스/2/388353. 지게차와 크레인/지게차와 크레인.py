from collections import deque

def solution(storage, requests):
    rows, cols = len(storage), len(storage[0])
    
    # 깔끔한 처리를 위해 패딩된 격자 만들기 (바깥을 '0'으로 감싸기)
    pad = [['0'] * (cols + 2) for _ in range(rows + 2)]
    for r in range(rows):
        for c in range(cols):
            pad[r+1][c+1] = storage[r][c] 
    
    # 외부 공기 BFS 함수: pad에서 바깥과 연결된 '0'을 True로 표시
    def mark_outside_air():
        air = [[False] * (cols + 2) for _ in range(rows + 2)]
        que = deque([(0,0)])
        air[0][0] = True
        
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        while que:
            r, c = que.popleft()
        
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                
                if 0 <= nr < rows + 2 and 0 <= nc < cols + 2 and pad[nr][nc] == '0' and not air[nr][nc]:
                    air[nr][nc] = True
                    que.append((nr,nc))
        return air         

    for req in requests:
        if len(req) == 2: # 크레인
            for r in range(1,rows+1):
                for c in range(1,cols+1):
                    if pad[r][c] == req[0]:
                        pad[r][c] = '0'
        else: # 지게차
            air = mark_outside_air()
            
            targets = []
            for r in range(1,rows+1):
                for c in range(1,cols+1):
                    if pad[r][c] == req:
                        if air[r-1][c] or air[r+1][c] or air[r][c-1] or air[r][c+1]:
                            targets.append((r,c))
            for r, c in targets:
                pad[r][c] = '0'
    remain = 0
    for r in range(1,rows+1):
        for c in range(1,cols+1):
            if pad[r][c] != '0':
                remain += 1

    return remain