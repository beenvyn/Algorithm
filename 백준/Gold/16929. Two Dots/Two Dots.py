import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
board = [input().strip() for _ in range(rows)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * cols for _ in range(rows)]

def backtrack(r, c, pr, pc, color):
    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        
        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == color:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                if backtrack(nr, nc, r, c, color):
                    return True
            else: # 이미 방문했는데 직전 칸이 아니면 사이클
                if not(nr == pr and nc == pc):
                    return True
    return False

for r in range(rows):
    for c in range(cols):
        if not visited[r][c]:
            visited[r][c] = True
            if backtrack(r, c, -1, -1, board[r][c]):
                print('Yes')
                sys.exit(0)

print('No')