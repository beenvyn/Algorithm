import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = 0
num_cnt = {}
r = 0

for l in range(N):
    while r < N and arr[r] not in num_cnt:
        num_cnt[arr[r]] = 1
        r += 1
    
    # 중복 없는 부분수열의 개수
    answer += (r - l)

    # l 삭제
    del num_cnt[arr[l]]

print(answer)  