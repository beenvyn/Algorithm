import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

answer = 0
visited = [[False] * cols for _ in range(rows)]
opts = [[(0, -1), (1, 0)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)]]

# 지금 보고있는 칸 번호, 현재까지의 총 점수
def dfs(idx, cur_sum):
    global answer

    # 0번칸부터 끝까지 본다
    if idx == rows * cols:
        answer = max(answer, cur_sum)
        return

    r, c = idx // cols, idx % cols

    # 이 칸을 부메랑의 중심으로 사용하는 경우
    if not visited[r][c]:
        for (dr1, dc1), (dr2, dc2) in opts:
            r1, c1 = r + dr1, c + dc1
            r2, c2 = r + dr2, c + dc2

            if (0 <= r1 < rows and 0 <= c1 < cols) and (0 <= r2 < rows and 0 <= c2 < cols) and not visited[r1][c1] and not visited[r2][c2]:
                visited[r][c] = visited[r1][c1] = visited[r2][c2] = True
                dfs(idx + 1, cur_sum + grid[r][c] * 2 + grid[r1][c1] + grid[r2][c2])
                visited[r][c] = visited[r1][c1] = visited[r2][c2] = False
    
    # 이 칸을 사용하지 않는 경우
    dfs(idx + 1, cur_sum)

dfs(0, 0)
print(answer)