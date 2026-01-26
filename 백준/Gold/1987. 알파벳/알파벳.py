import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
board = [list(input().strip()) for _ in range(rows)]

chars = set()
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = 0

def dfs(r, c, cnt):
    global answer
    answer = max(answer, cnt)

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if board[nr][nc] not in chars:
                chars.add(board[nr][nc])
                dfs(nr, nc, cnt + 1)
                chars.remove(board[nr][nc])
            
chars.add(board[0][0])
dfs(0, 0, 1)

print(answer)