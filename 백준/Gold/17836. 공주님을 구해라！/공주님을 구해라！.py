import sys
from collections import deque
input = sys.stdin.readline

rows, cols, time = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(rows)]

visited = [[[0] * 2 for _ in range(cols)] for _ in range(rows)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

que = deque([(0,0,0,0)])
visited[0][0][0] = True
answers = []

while que:
    r, c, dist, flag = que.popleft()

    if r == rows - 1 and c == cols - 1:
        if dist <= time:
            answers.append(dist)
    
    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols:
            # 칼이 있는 경우
            if flag:
                if not visited[nr][nc][1]:
                    que.append((nr, nc, dist + 1, 1))
                    visited[nr][nc][1] = 1
            else:
                if not visited[nr][nc][0]:
                    if graph[nr][nc] == 2:
                        que.append((nr, nc, dist + 1, 1))
                        visited[nr][nc][0] = 1
                    elif graph[nr][nc] == 0:
                        que.append((nr, nc, dist + 1, flag))
                        visited[nr][nc][0] = 1

print(min(answers)) if answers else print('Fail')             