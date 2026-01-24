import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dishes = [int(input().rstrip()) for _ in range(N)]

dishes.extend(dishes[:k]) # 원형 처리 
answer = 0
sushi_cnt = {}

# 초기 k개 세팅
for i in range(k):
    if dishes[i] not in sushi_cnt:
        sushi_cnt[dishes[i]] = 0
    sushi_cnt[dishes[i]] += 1

l, r = 0, k

for _ in range(N): # 원도우 N개만 확인 
    cnt = len(sushi_cnt.keys())
    if c not in sushi_cnt:
        cnt += 1

    answer = max(answer, cnt)

    if dishes[r] not in sushi_cnt:
        sushi_cnt[dishes[r]] = 0
    sushi_cnt[dishes[r]] += 1
    r += 1

    sushi_cnt[dishes[l]] -= 1
    if sushi_cnt[dishes[l]] == 0:
        del sushi_cnt[dishes[l]]
    l += 1

print(answer)