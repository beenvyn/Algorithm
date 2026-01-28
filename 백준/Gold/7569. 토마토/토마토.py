import sys
from collections import deque
input = sys.stdin.readline

cols, rows, height = map(int, input().split())
board = []
for _ in range(height):
    floor = [list(map(int, input().split())) for _ in range(rows)]
    board.append(floor)

dirs = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)]
days = 0
que = deque([])

for h in range(height):
    for r in range(rows):
        for c in range(cols):
            if board[h][r][c] == 1:
                que.append([h, r, c])

while que:
    for _ in range(len(que)):
        h, r, c = que.popleft()

        for d in dirs:
            nh, nr, nc = h + d[0], r + d[1], c + d[2]

            if 0 <= nh < height and 0 <= nr < rows and 0 <= nc < cols and board[nh][nr][nc] == 0:
                board[nh][nr][nc] = 1
                que.append([nh, nr, nc])
    days += 1

for floor in board:
    for row in floor:
        if not all(row):
            print(-1)
            sys.exit()

print(days - 1)