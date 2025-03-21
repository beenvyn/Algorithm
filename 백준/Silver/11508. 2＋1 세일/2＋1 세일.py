import sys
input = sys.stdin.readline

n = int(input())
prices = [int(input()) for _ in range(n)]
prices = sorted(prices, reverse=True)
answer = 0

for i in range(0,len(prices),3):
    group = prices[i:i+3]
    answer += sum(group)
    if len(group) == 3:
        answer -= group[-1]

print(answer)