from collections import deque

def solution(board):
    n = len(board)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # dist[r][c][d] : d방향으로 (r, c)에 도착했을 때 최소 비용
    dist = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    que = deque()
    
    # 시작점에서는 4방향 모두 비용 0으로 시작
    for d in range(4):
        dist[0][0][d] = 0
        que.append((0, 0, d, 0))
    
    while que:
        r, c, direction, cost = que.popleft()
        
        for nd in range(4):
            nr, nc = r + dirs[nd][0], c + dirs[nd][1]
            
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            
            if board[nr][nc] == 1:
                continue
            
            new_cost = cost + 100
            
            if nd != direction: # 다른 방향이면 코너 발생
                new_cost += 500
            
            if new_cost < dist[nr][nc][nd]:
                dist[nr][nc][nd] = new_cost
                que.append((nr, nc, nd, new_cost))
        
    return min(dist[n - 1][n - 1])