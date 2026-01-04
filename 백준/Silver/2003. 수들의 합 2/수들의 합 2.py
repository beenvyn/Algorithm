import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0 # r은 다음에 포함할 위치
total = 0
answer = 0

while True:
    if total >= M:
        if total == M:
            answer += 1
        total -= arr[l]
        l += 1
    else:
        if r == N:
            break
        total += arr[r]
        r += 1

print(answer)