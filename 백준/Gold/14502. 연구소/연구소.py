import sys
from itertools import combinations
input = sys.stdin.readline

rows, cols = map(int, input().split())
board = [input().split() for _ in range(rows)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
blanks = []
viruses = [] 
answer = 0

for r in range(rows):
    for c in range(cols):
        if board[r][c] == '0':
            blanks.append((r,c))
        elif board[r][c] == '2':
            viruses.append((r,c))

walls = combinations(blanks, 3)

def virus(r,c,board,visited):
    for d in dirs:
        nvr, nvc = r + d[0], c + d[1]

        if 0 <= nvr < rows and 0 <= nvc < cols and board[nvr][nvc] == '0' and not visited[nvr][nvc]:
            visited[nvr][nvc] = True
            board[nvr][nvc] = '2'
            virus(nvr,nvc,board,visited)

# 모든 벽의 경우의 수 탐색
for wall in walls:
    new_board = [row[:] for row in board]
    visited = [[False] * cols for _ in range(rows)]
    cnt = 0

    for r, c in wall:
        new_board[r][c] = '1'
    
    # 바이러스 퍼진 보드 만들기
    for vr, vc in viruses:
        visited[vr][vc] = True
        virus(vr,vc,new_board,visited)
    
    # 안전 영역 계산
    for row in new_board:
        cnt += row.count('0')
    
    answer = max(answer,cnt)

print(answer)