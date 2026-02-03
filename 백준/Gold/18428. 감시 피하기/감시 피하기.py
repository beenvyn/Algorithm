import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().split()) for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 빈칸, 선생님 전부 저장
spaces = []
teachers = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 'X':
            spaces.append([r, c])
        elif board[r][c] == 'T':
            teachers.append([r, c])
            
def watch():
    for teacher in teachers:
        r, c = teacher

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            while 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 'O':
                    break

                if board[nr][nc] == 'S':
                    return False
                
                nr += dr
                nc += dc

    return True
                    
def change(places, val):
    for r, c in places:
        board[r][c] = val

# 위치 3개 고르기
def dfs(idx, cur):
    if len(cur) == 3:
        change(cur, "O")
        if watch():
            print('YES')
            sys.exit()
        change(cur, 'X')
        return

    for i in range(idx, len(spaces)):
        cur.append(spaces[i])
        dfs(i + 1, cur)
        cur.pop()
        
dfs(0, [])
print('NO')