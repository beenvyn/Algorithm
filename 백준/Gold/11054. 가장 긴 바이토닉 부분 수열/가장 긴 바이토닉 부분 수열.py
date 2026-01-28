import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

inc = [1] * N # inc[i]: arr[i]에서 끝나는 최장 증가 부분수열 길이
dec = [1] * N # dec[i]: arr[i]에서 시작하는 최장 감소 부분수열 길이

# inc 구하기
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j] + 1)

# dec 구하기
for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if arr[i] > arr[j]:
            dec[i] = max(dec[i], dec[j] + 1)

# 각 i를 “꼭대기(peak)”로 두고
# (i까지의 LIS 길이) + (i부터의 LDS 길이) - 1 의 최댓값
answer = 0
for i in range(N):
    answer = max(answer, inc[i] + dec[i] - 1)

print(answer)