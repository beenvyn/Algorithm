import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)] # ([내구도, 무게])
answer = 0

# 손에 든 계란의 순서, 깨진 계란 수
def dfs(idx, broken):
    global answer
    if idx == N:
        answer = max(answer, broken)
        return
    
    if eggs[idx][0] <= 0: # 현재 손에 든 계란이 깨진 경우
        dfs(idx + 1, broken) # 다음 계란으로 넘기기
        return
    
    hit = False # 이번 idx에서 한 번이라도 쳤는지
    
    # 현재 손에 든 계란이 안깨진 경우
    for j in range(N):
        if j != idx and eggs[j][0] > 0: # 칠 수 있는 계란 찾기
            hit = True
            before_j, before_idx = eggs[j][0], eggs[idx][0] # 기존 내구도 저장
            after_j, after_idx = eggs[j][0] - eggs[idx][1], eggs[idx][0] - eggs[j][1]
            eggs[j][0], eggs[idx][0] = after_j, after_idx
            newly_broken = 0
            if eggs[j][0] <= 0:
                newly_broken += 1
            if eggs[idx][0] <= 0:
                newly_broken += 1
            dfs(idx + 1, broken + newly_broken)
            eggs[j][0], eggs[idx][0] = before_j, before_idx # 내구도 원복

    if not hit: # 칠 수 있는 계란이 없으면 
        dfs(idx + 1, broken) # 다음 계란으로 넘기기

dfs(0,0)
print(answer)