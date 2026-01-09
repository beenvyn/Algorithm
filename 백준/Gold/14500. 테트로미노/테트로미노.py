import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

visited = [[False] * cols for _ in range(rows)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

# 'ㅜ'를 제외한 다른 모양들은 상하좌우로 4칸만 밟으면 다 만들어짐
def dfs(r, c, cnt, cur_sum):
    global answer
    
    if cnt == 4:
        answer = max(answer, cur_sum)
        return

    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, cnt + 1, cur_sum + grid[nr][nc])
            visited[nr][nc] = False

# 'ㅗ' 모양(ㅗ/ㅜ/ㅓ/ㅏ)만 따로 처리
# 'ㅗ' 모양은 가운데 칸이 1개 있고 그 중심과 상하좌우로 붙어있는 칸들 중 3개를 더 붙임.
def check_t(r, c):
    global answer
    center = grid[r][c] # 'ㅗ'의 가운데 고정
    neigh = []

    # 중심의 상하좌우 값들을 모으기
    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < rows and 0 <= nc < cols:
            neigh.append(grid[nr][nc])
    
    if len(neigh) >= 3: # 중심이 가장자리면 상하좌우가 3개만 나오고 그게 아니면 4개가 나옴.
        neigh.sort(reverse=True)
        answer = max(answer, center + neigh[0] + neigh[1] + neigh[2]) # 가장 큰 상하좌우 값 3개 선택
        
# 시작점 전달
for r in range(rows):
    for c in range(cols):
        visited[r][c] = True
        dfs(r, c, 1, grid[r][c])
        visited[r][c] = False
        # 'ㅗ' 모양 확인
        check_t(r,c)
print(answer)