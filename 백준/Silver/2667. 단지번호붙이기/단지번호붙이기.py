import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = []

def bfs(map, i, j):
    queue = deque();

    queue.append([i,j])
    map[i][j] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < n) and (0 <= ny < n):
                if map[nx][ny] == 1:
                    queue.append([nx, ny])
                    map[nx][ny] = 0
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt = bfs(map,i,j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for c in answer:
    print(c)