from collections import Counter

n = int(input())
cards = Counter(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

answer = [cards[c] for c in check]

print(' '.join(map(str,answer)))