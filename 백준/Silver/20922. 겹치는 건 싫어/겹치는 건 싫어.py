import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

num_dict = {}
l, r = 0, 0 # r은 다음에 포함할 인덱스
answer = 0

while r < N:
    x = arr[r]
    if x not in num_dict:
        num_dict[x] = 0
    num_dict[x] += 1
    r += 1

    while num_dict[x] > K: # K개 이하가 될 때까지 이동
        num_dict[arr[l]] -= 1
        l += 1
    answer = max(answer, r - l)
    
print(answer)