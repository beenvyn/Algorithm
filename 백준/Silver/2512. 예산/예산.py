import sys
input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
M = int(input())

if sum(req) <= M:
    print(max(req))
    sys.exit()

# 총 예산 계산
def get_total(k):
    total = 0
    for r in req:
        if r < k:
            total += r
        else:
            total += k
    return total

# 상한액 정하기
answer = 0
l, r = 0, 1000000000

while l <= r:
    k = (l + r) // 2
    res = get_total(k)
    
    if res > M:
        r = k - 1
    else:
        answer = max(answer, k)
        l = k + 1

print(answer)