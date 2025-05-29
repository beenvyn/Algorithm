from collections import deque
import sys

input = sys.stdin.readline

row, col = map(int, input().split())
grid = []
for _ in range(row):
    grid.append(input().rstrip())

def bfs(row,col,grid):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # 다음 위치 계산
    def move(x,y,dir):
        nx, ny = x, y
        while True:
            nx = nx + dx[dir]
            ny = ny + dy[dir]

            if grid[nx][ny] == 'O':
                break

            if grid[nx][ny] == '#':
                nx -= dx[dir]
                ny -= dy[dir]
                break

        return (nx, ny)
    
    # red, blue 시작 위치 찾기
    for x in range(row):
        for y in range(col): 
            if grid[x][y] == 'R':
                rx, ry = x, y
            if grid[x][y] == 'B':
                bx, by = x, y

    # queue에 시작점 예약 (red좌표, blue좌표, cnt)
    visited = set()
    q = deque([(rx,ry,bx,by,0)])
    visited.add((rx,ry,bx,by,0))

    while q:
        # 현재 위치 방문
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            return 0

        # 빨간 구슬이 구멍에 빠진 경우
        if grid[rx][ry] == 'O':
            return 1

        for dir in range(4):
            nrx, nry = move(rx,ry,dir)
            nbx, nby = move(bx,by,dir)

            if grid[nbx][nby] == 'O':
                continue
            
            # 만약 red, blue 위치가 같으면 조정
            if nrx == nbx and nry == nby:
                # 빨간 구슬이 더 멀리 있는 경우
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nrx -= dx[dir]
                    nry -= dy[dir]
                else: # 파란 구슬이 더 멀리 있는 경우
                    nbx -= dx[dir]
                    nby -= dy[dir]
        
            if (nrx, nry, nbx, nby) not in visited:
                q.append((nrx, nry, nbx, nby, cnt + 1))
                visited.add((nrx, nry, nbx, nby))
    return 0

print(bfs(row,col,grid))

        