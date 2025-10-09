import sys
from collections import deque
# sys.setrecursionlimit(300000)
input = sys.stdin.readline

rows, cols = map(int, input().split())
graph = [input() for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        if graph[r][c] == 'R':
            rsr, rsc = r, c
        elif graph[r][c] == 'B':
            bsr, bsc = r, c

visited = set()
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
que = deque([(rsr,rsc,bsr,bsc,0)])
visited.add((rsr,rsc,bsr,bsc))

def move(r,c,dir):
    nr, nc = r, c
    while True:
        nr += dirs[dir][0]
        nc += dirs[dir][1]

        if graph[nr][nc] == '#':
            nr -= dirs[dir][0]
            nc -= dirs[dir][1]
            break
        elif graph[nr][nc] == 'O':
            break

    return (nr, nc)


while que:
    rr, rc, br, bc, cnt = que.popleft()

    if cnt >= 10:
        continue
    
    for dir in range(4):
        nrr, nrc = move(rr,rc,dir)
        nbr, nbc = move(br,bc,dir)

        if graph[nbr][nbc] == 'O':
            continue

        if graph[nrr][nrc] == 'O':
            print(1)
            sys.exit(0)
        
        if nrr == nbr and nrc == nbc:
            if abs(nrr - rr) + abs(nrc - rc) < abs(nbr - br) + abs(nbc - bc):
                nbr -= dirs[dir][0]
                nbc -= dirs[dir][1]
            else:
                nrr -= dirs[dir][0]
                nrc -= dirs[dir][1]

        if (nrr,nrc,nbr,nbc) not in visited:        
            que.append((nrr,nrc,nbr,nbc,cnt + 1))
            visited.add((nrr,nrc,nbr,nbc))

print(0)
        
