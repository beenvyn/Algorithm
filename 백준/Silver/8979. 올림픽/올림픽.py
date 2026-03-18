import sys
input = sys.stdin.readline

N, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]

infos.sort(key=lambda x:x[0])
_, g, s, b = infos[K-1]

# k국가 보다 높은 랭킹의 국가 수 찾기
cnt = 1
for i in range(N):
    if infos[i][0] != K:
        if infos[i][1] > g or (infos[i][1] == g and infos[i][2]) > s or (infos[i][1] == g and infos[i][2] == s and infos[i][3] > b):
            cnt += 1 

print(cnt)