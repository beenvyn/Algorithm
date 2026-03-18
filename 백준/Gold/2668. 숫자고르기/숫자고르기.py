import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + [int(input()) for _ in range(N)]

# 사이클을 찾는 문제
# 출발한 숫자에서 시작해서 계속 따라갔을 때 다시 자기 자신으로 돌아오는 숫자들
answer = []

def dfs(start, cur, visited):
    # 현재 숫자를 이번 탐색 경로에 추가
    visited.append(cur)
    nxt = nums[cur]

    # 다음 숫자가 처음 시작한 숫자 start라면
    # start -> ... -> start 형태의 사이클이 만들어진 것
    if nxt == start:
        answer.extend(visited)
        return
    
    # 이미 visited 안에 있으면,
    # start로 돌아온 게 아니라 다른 곳에서 사이클이 난 것이므로 종료
    if nxt not in visited:
        dfs(start, nxt, visited)

# 모든 숫자를 시작점으로 해서 검사
for i in range(1, N + 1):
    dfs(i, i, [])

answer = sorted(set(answer))
print(len(answer))
for x in answer:
    print(x)