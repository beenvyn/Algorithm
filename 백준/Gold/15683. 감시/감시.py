import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(rows)]

# 1번: 4가지, 2번: 2가지, 3번: 4가지, 4번: 4가지, 5번: 1가지
dirs = {
    1: [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    2: [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
}

cctvs = []
for r in range(rows):
    for c in range(cols):
        if board[r][c] in range(1, 6):
            cctvs.append([r, c, board[r][c]])

answer = float('inf')

# 감시 표시 함수
def watch(r, c, dir_list):
    changed = [] # 여기 저장한 좌표들만 원복하면 됨

    for dr, dc in dir_list:
        nr, nc = r + dr, c + dc
        while 0 <= nr < rows and 0 <= nc < cols:
            if board[nr][nc] == 6: # 벽 만나면 종료
                break

            if board[nr][nc] == 0: # 빈칸만 감시 처리
                board[nr][nc] = -1
                changed.append([nr, nc])
            
            # cctv(1~5)나 이미 감시된 곳(-1)은 통과 
            nr += dr
            nc += dc

    return changed

# 복구 함수
def unwatch(changed):
    for r, c in changed:
        board[r][c] = 0

# 사각지대 개수 세는 함수
def get_cnt():
    cnt = 0
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 0:
                cnt += 1
    return cnt

# CCTV 회전 케이스 선택
def dfs(idx):
    global answer

    if idx == len(cctvs):
        answer = min(answer, get_cnt())
        return

    r, c, t = cctvs[idx]

    for case in dirs[t]:
        changed = watch(r, c, case)
        dfs(idx + 1)
        unwatch(changed)

dfs(0)
print(answer)