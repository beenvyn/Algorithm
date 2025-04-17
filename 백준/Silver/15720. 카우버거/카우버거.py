b, s, d = map(int, input().split())
prices = []

for _ in range(3):
    prices.append(sorted(list(map(int, input().split())), reverse=True))

before = 0
for price in prices:
    before += sum(price)

total = 0
min_num = min(b, s, d)
for i in range(min_num):
    temp = 0
    temp += prices[0][i]
    temp += prices[1][i]
    temp += prices[2][i]
    temp *= 0.9
    total += int(temp)

for price in prices:
    if len(price) > min_num:
        price.sort()
        for num in price[:len(price) - min_num]:
            total += num

print(before)
print(total)