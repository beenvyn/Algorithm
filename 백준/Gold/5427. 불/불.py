import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for _ in range(T):
    cols, rows = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(rows)]

    man_q = deque()
    fire_q = deque()
    visited = [[False] * cols for _ in range(rows)]
    success = False

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                man_q.append((r, c, 0))
                visited[r][c] = True
            elif grid[r][c] == '*':
                fire_q.append((r, c))
    
    while man_q:
        # 불 처리
        for _ in range(len(fire_q)):
            fr, fc = fire_q.popleft()

            for d in dirs:
                nfr, nfc = fr + d[0], fc + d[1]

                if 0 <= nfr < rows and 0 <= nfc < cols and grid[nfr][nfc] in ['.', '@']:
                    grid[nfr][nfc] = '*'
                    fire_q.append((nfr, nfc))
        
        # 사람 처리
        for _ in range(len(man_q)):
            mr, mc, time = man_q.popleft()
            
            if mr == 0 or mr == rows - 1 or mc == 0 or mc == cols - 1:
                print(time + 1)
                success = True
                break # for문 탈출 

            for d in dirs:
                nmr, nmc = mr + d[0], mc + d[1]

                if 0 <= nmr < rows and 0 <= nmc < cols and not visited[nmr][nmc] and grid[nmr][nmc] == '.':
                    visited[nmr][nmc] = True
                    man_q.append((nmr, nmc, time + 1))
        
        if success: # 성공했을 경우 while문도 탈출
            break

    if not success:
        print('IMPOSSIBLE')