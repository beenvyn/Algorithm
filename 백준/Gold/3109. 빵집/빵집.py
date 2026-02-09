import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(input().strip()) for _ in range(rows)]

# 중요: 오른쪽위, 오른쪽, 오른쪽아래 -> 전체 개수가 최대가 됨
dirs = [(-1, 1), (0, 1), (1, 1)]
visited = [[False] * cols for _ in range(rows)]

def dfs(r, c):
    # 마지막 열 도착 = 이 파이프 성공
    if c == cols - 1:
        return True
    
    for d in dirs:
        nr, nc = r + d[0], c + d[1]

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.' and not visited[nr][nc]:
            visited[nr][nc] = True # 지나간 칸은 즉시 잠금(복구 X)
            if dfs(nr, nc):
                return True
    return False

answer = 0
for start in range(rows):
    if grid[start][0] == '.':
        visited[start][0] = True
        if dfs(start, 0):
            answer += 1

print(answer)