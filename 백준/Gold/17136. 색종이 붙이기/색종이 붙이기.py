import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(10)]
possible = [5, 5, 5, 5, 5]
answer = 26

# 주어진 영역이 전부 1인지 확인
def checkRC(r, nr, c, nc):
    for i in range(r, nr + 1):
        for j in range(c, nc + 1):
            if grid[i][j] == 0:
                return False
    return True

# val로 주어진 영역 덮어쓰기
def attach(r, nr, c, nc, val):
    for i in range(r, nr + 1):
        for j in range(c, nc + 1):
            grid[i][j] = val

# 완탐 함수
# 지금까지 사용한 색종이 개수
def backtrack(used):
    global answer
    
    # 가지치기: 이미 현재 최적(answer)보다 많이 썼으면 더 볼 필요 없음
    if used >= answer:
        return
    
    # 보드 위 왼쪽부터 스캔
    for r in range(10):
        for c in range(10):
             # 아직 덮지 못한 칸을 발견하면 그 칸을 반드시 덮어야 함
            if grid[r][c]:
                # 색종이 크기별로 큰 것부터 시도
                for k in range(4, -1, -1):
                    nr, nc = r + k, c + k
                    # 해당 크기의 색종이가 남았고 보드 밖으로 안나가는지 확인 
                    if possible[k] and nr < 10 and nc < 10:
                        # 해당 영역이 전부 1인지 체크
                        if checkRC(r, nr, c, nc):
                            attach(r, nr, c, nc, 0) # 해당 영역 0으로 덮기
                            possible[k] -= 1
                            backtrack(used + 1) 
                            attach(r, nr, c, nc, 1) # 지금 크기를 붙여봤으니 다른 선택지(다른 크기/배치)를 시도해보기 위해 상태를 되롤림 
                            possible[k] += 1
                # (r,c)에서 붙일 수 있는 모든 경우를 시도해봄
                return
    # 끝까지 1이 없으면 다 덮은 상태
    answer = min(answer, used)

backtrack(0)
print(answer if answer != 26 else -1)