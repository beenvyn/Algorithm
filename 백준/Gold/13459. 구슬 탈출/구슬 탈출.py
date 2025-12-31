from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(r, c, d):
    nr, nc = r, c
    while True:
        nr += dirs[d][0]
        nc += dirs[d][1]

        if grid[nr][nc] == 'O':
            break

        if grid[nr][nc] == '#':
            nr -= dirs[d][0]
            nc -= dirs[d][1]
            break
    return (nr, nc)

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'R':
            rr, rc = r, c
        elif grid[r][c] == 'B':
            br, bc = r, c

que = deque([(rr, rc, br, bc, 0)])
visited = set()
visited.add((rr, rc, br, bc))

while que:
    rr, rc, br, bc, cnt = que.popleft()

    if cnt > 10:
        print(0)
        sys.exit()
    
    if grid[rr][rc] == 'O':
        print(1)
        sys.exit()

    for d in range(4):
        nrr, nrc = move(rr, rc, d)
        nbr, nbc = move(br, bc, d)

        if grid[nbr][nbc] == 'O':
            continue

        if nrr == nbr and nrc == nbc:
            if abs(nrr - rr) + abs(nrc - rc) > abs(nbr - br) + abs(nbc - bc):
                nrr -= dirs[d][0]
                nrc -= dirs[d][1]
            else:
                nbr -= dirs[d][0]
                nbc -= dirs[d][1]
        
        if (nrr, nrc, nbr, nbc) not in visited:
            que.append((nrr, nrc, nbr, nbc, cnt + 1))
            visited.add((nrr, nrc, nbr, nbc))

print(0)
    