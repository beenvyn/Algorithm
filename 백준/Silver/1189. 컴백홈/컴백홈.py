import sys
input = sys.stdin.readline

rows, cols, k = map(int, input().split())
board = [input().strip() for _ in range(rows)]

visited = [[False] * cols for _ in range(rows)]
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = 0

def dfs(r, c, cnt):
    global answer

    if cnt > k:
        return
    
    if cnt == k and r == 0 and c == cols - 1:
        answer += 1
        return

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] != 'T':
            visited[nr][nc] = True
            dfs(nr, nc, cnt + 1)
            visited[nr][nc] = False

visited[rows - 1][0] = True
dfs(rows - 1, 0, 1)

print(answer)