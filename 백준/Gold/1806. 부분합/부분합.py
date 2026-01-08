import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 1 # right는 다음에 포함할 원소의 인덱스
total = arr[left]
answer = N + 1 # 부분 수열의 길이는 무조건 이거 이하임.

while True:
    if total < S:
        if right == N:
            break
        total += arr[right]
        right += 1
    else:
        answer = min(answer, right - left)
        total -= arr[left]
        left += 1

print(0 if answer == N + 1 else answer)