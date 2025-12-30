from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]

man_q = deque()
fire_q = deque()
visited = [[False] * C for _ in range(R)]

# 초기 위치 찾기
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'J':
            man_q.append((r,c,0))
            visited[r][c] = True
        elif grid[r][c] == 'F':
            fire_q.append((r,c))

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

while man_q:
    # 불 확산 -> 현재 시간대의 불만 처리하기 위해 for 문 사용
    for _ in range(len(fire_q)):
        r, c = fire_q.popleft()

        for d in dirs:
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in ['.', 'J']:
                grid[nr][nc] = 'F'
                fire_q.append((nr,nc)) # 다음에 번질 불 예약
    
    # 사람 이동 -> 현재 시간대의 사람만 처리하기 위해 for 문 사용
    for _ in range(len(man_q)):
        r, c, time = man_q.popleft()

        # 탈출 성공
        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            print(time + 1)
            sys.exit()
        
        for d in dirs:
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.' and not visited[nr][nc]:
                man_q.append((nr, nc, time + 1))
                visited[nr][nc] = True

print('IMPOSSIBLE')