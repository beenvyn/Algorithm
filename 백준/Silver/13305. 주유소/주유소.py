n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = distances[0] * prices[0]
min_price = prices[0]

for i in range(1, n - 1):
    if prices[i] < min_price:
        answer += prices[i] * distances[i]
        min_price = prices[i]
    else:
        answer += min_price * distances[i]

print(answer)