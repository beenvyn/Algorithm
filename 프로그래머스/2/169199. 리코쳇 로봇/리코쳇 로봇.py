from collections import deque

def solution(board):
    answer = 0
    rows, cols = len(board), len(board[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * cols for _ in range(rows)] # 멈출 수 있는 위치만 방문 여부 체크 대상임
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                sr, sc = r, c
                
    # 한 방향으로 끝까지 미끄러지는 함수
    def move(r, c, dir_idx):
        while 0 <= r < rows and 0 <= c < cols and board[r][c] != 'D':
            r += dirs[dir_idx][0]
            c += dirs[dir_idx][1]
        
        r -= dirs[dir_idx][0]
        c -= dirs[dir_idx][1]
        
        return r, c
    
    que = deque([(sr, sc, 0)])
    visited[sr][sc] = True

    while que:
        r, c, cnt = que.popleft()
        
        if board[r][c] == 'G':
            return cnt
        
        for i in range(4):
            # 해당 방향으로 끝까지 미끄러진 위치
            nr, nc = move(r, c, i)

            if not visited[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc, cnt + 1))
    
    return -1