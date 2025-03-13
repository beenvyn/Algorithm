n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = sorted(coins, reverse=True)
answer = 0

for c in coins:
    if c > k:
        continue
    answer += k // c
    k %= c

print(answer)