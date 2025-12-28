import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

cards.sort()
answer = 0

if n == 1:
    print(0)
    sys.exit(0)

heapq.heapify(cards)

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    res = a + b
    answer += res
    heapq.heappush(cards, res)

print(answer)