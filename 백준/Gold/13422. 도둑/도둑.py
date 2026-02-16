import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))

    if N == M:
        print(1 if sum(houses) < K else 0)
        continue

    houses.extend(houses[:M-1])

    total = sum(houses[:M])
    answer = 1 if total < K else 0

    for l in range(1, N):
        total -= houses[l - 1]
        total += houses[l + M - 1]

        if total < K:
            answer += 1

    print(answer)