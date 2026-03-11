from collections import deque
'''
석유 덩어리 하나를 DFS/BFS로 한 번만 탐색하면서
그 덩어리의 크기(area) 를 구하고
그 덩어리가 걸쳐 있는 열들을 모은 다음
그 열들에다가 area를 한 번씩 더해주기
'''

def solution(land):
    answer = 0
    rows, cols = len(land), len(land[0])
    visited = [[False] * cols for _ in range(rows)]
    
    col_oils = [0] * cols # 열별 석유량
    dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    
    def bfs(r, c):
        que = deque([(r, c)])
        visited[r][c] = True
        
        area = 1
        used_cols = {c}
        
        while que:
            r, c = que.popleft()
            
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                
                if 0 <= nr < rows and 0 <= nc < cols and land[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    area += 1
                    que.append((nr, nc))
                    used_cols.add(nc)
                    
        return area, used_cols
    
    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1 and not visited[r][c]:
                area, used_cols = bfs(r, c)
                for col in used_cols:
                    col_oils[col] += area
    
    return max(col_oils)