import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start, end = 0, 1
sum = arr[0]

while True:
    if sum < m:
        if end < n:
            sum += arr[end]
            end += 1
        else:
            break
    elif sum > m:
        sum -= arr[start]
        start += 1
    else:
        sum -= arr[start]
        start += 1
        answer += 1

print(answer)