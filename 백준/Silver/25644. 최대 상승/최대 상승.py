n = int(input())
stocks = list(map(int, input().split()))

benefit = 0
result = 0

for i in range(n - 1, -1, -1):
    benefit = max(benefit, stocks[i])
    result = max(benefit - stocks[i], result)

print(result)