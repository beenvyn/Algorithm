import sys
from collections import Counter

input = sys.stdin.readline
n , m = map(int, input().rstrip().split())
words = []

for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

counter = Counter(words)
sorted_words = sorted(counter.keys(), key=lambda x:(-counter[x],-len(x),x))

for w in sorted_words:
    print(w)