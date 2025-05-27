from collections import deque
import sys

input = sys.stdin.readline
dist = 1
row, col = map(int, input().split())
graph = [input().strip() for _ in range(row)]

visited = [[[False, False] for _ in range(col)] for _ in range(row)]

q = deque([(0,0,1,1)])
visited[0][0][1] = True

dr = [0,0,-1,1]
dc = [-1,1,0,0]

while q:
    r, c, flag, dist = q.popleft()

    if r == row - 1 and c == col - 1:
        print(dist)
        sys.exit()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < row and 0 <= nc < col:
            if graph[nr][nc] == '0' and not visited[nr][nc][flag]:
                q.append((nr,nc,flag,dist+1))
                visited[nr][nc][flag] = True
            
            # 벽 부수기 
            elif graph[nr][nc] == '1' and flag == 1 and not visited[nr][nc][0]:
                q.append((nr,nc,0,dist+1))
                visited[nr][nc][0] = True
else:
    print(-1)