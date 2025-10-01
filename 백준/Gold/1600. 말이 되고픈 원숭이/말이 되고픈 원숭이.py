import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
cols, rows = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]
visited = [[[0] * (k + 1) for _ in range(cols)] for _ in range(rows)]
answer = 0

m_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
h_dirs = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
    print(-1)
    sys.exit(0)

que = deque([(0,0,k)])
visited[0][0][k] = 1

while que:
    for _ in range(len(que)):
        r, c, flag = que.popleft()

        if r == rows - 1 and c == cols - 1:
            print(answer)
            sys.exit(0)

        # 특수 점프
        if flag > 0:
            for d in h_dirs:
                hr, hc = r + d[0], c + d[1]

                if 0 <= hr < rows and 0 <= hc < cols and grid[hr][hc] == 0 and not visited[hr][hc][flag-1]:
                    que.append((hr,hc,flag-1))
                    visited[hr][hc][flag-1] = True
        
        # 일반 점프
        for d in m_dirs:
            mr, mc = r + d[0], c + d[1]

            if 0 <= mr < rows and 0 <= mc < cols and grid[mr][mc] == 0 and not visited[mr][mc][flag]:
                que.append((mr,mc,flag))
                visited[mr][mc][flag] = True
    
    answer += 1

print(-1)

