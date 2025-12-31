from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]

h_que = deque()
w_que = deque()
visited = [[False] * C for _ in range(R)]
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# 초기 위치 찾기
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            visited[r][c] = True
            h_que.append((r, c, 0))
        elif grid[r][c] == '*':
            w_que.append((r, c))

while h_que:
    # 현 시간대에서 물이 번지는 것 처리
    for _ in range(len(w_que)):
        r, c = w_que.popleft()

        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in ['.', 'S']:
                grid[nr][nc] = '*'
                w_que.append((nr, nc))
    
    # 현 시간대에서 고슴도치 이동 처리
    for _ in range(len(h_que)):
        r, c, time = h_que.popleft()

        if grid[r][c] == 'D':
            print(time)
            sys.exit()
        
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in ['.', 'D'] and not visited[nr][nc]:
                visited[nr][nc] = True
                h_que.append((nr, nc, time + 1))

print('KAKTUS')