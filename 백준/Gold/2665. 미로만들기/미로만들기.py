import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[float('inf')] * n for _ in range(n)]

dist[0][0] = 0
que = deque([(0, 0)])

while que:
    r, c = que.popleft()

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < n and 0 <= nc < n:
            # 흰 방이면 비용 0, 검은 방이면 비용 1
            w = 0 if board[nr][nc] == '1' else 1
            nd = dist[r][c] + w

            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                
                if w == 0: # 공짜 길은 먼저 탐색 
                    que.appendleft((nr, nc)) 
                else: # 돈 드는 길은 나중에 탐색 
                    que.append((nr, nc))

print(dist[n - 1][n - 1])