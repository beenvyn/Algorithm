n = int(input())
a, b = map(int, input().split())
c = int(input())
toppings = [int(input()) for _ in range(n)]
toppings.sort(reverse=True)

result = c // a
cal = c
price = a

for i in range(n):
    cal += toppings[i]
    price += b
    result = max(result, cal // price)
    
print(result)