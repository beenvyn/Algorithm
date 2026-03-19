import sys
input = sys.stdin.readline

N = int(input())
grid = [input().rstrip() for _ in range(N)]

dirs = [(0, -1), (0, 1), (1, 0)]
length = [0] * 5

# 심장 위치
hr, hc = 0, 0
for r in range(1, N - 1):
    for c in range(1, N - 1):
        if grid[r][c] == '*' and grid[r-1][c] == '*' and grid[r][c-1] == '*' and grid[r][c+1] == '*' and grid[r+1][c] == '*':
            hr, hc = r, c

def get_length(sr, sc, dir_idx):
    length = 1
    nr, nc = sr + dirs[dir_idx][0], sc + dirs[dir_idx][1]
    
    while 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '*':
        length += 1
        nr += dirs[dir_idx][0]
        nc += dirs[dir_idx][1]
    
    return nr, nc, length

# 왼쪽 팔
_, _, l = get_length(hr, hc - 1, 0)
length[0] = l

# 오른쪽 팔
_, _, l = get_length(hr, hc + 1, 1)
length[1] = l

# 허리
wr, wc, l = get_length(hr + 1, hc, 2)
length[2] = l

# 왼쪽 다리
_, _, l = get_length(wr, wc - 1, 2)
length[3] = l

# 오른쪽 다리
_, _, l = get_length(wr, wc + 1, 2)
length[4] = l

print(hr + 1, hc + 1)
print(*length)