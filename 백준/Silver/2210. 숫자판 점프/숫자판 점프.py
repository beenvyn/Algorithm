import sys
input = sys.stdin.readline

board = [input().split() for _ in range(5)]
answers = set()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c, cur):
    if len(cur) == 6:
        answers.add(cur)
        return

    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, cur + board[nr][nc])

for r in range(5):
    for c in range(5):
        dfs(r, c, board[r][c])

print(len(answers))