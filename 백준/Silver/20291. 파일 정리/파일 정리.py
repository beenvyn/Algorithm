import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
files = [input().strip().split('.')[1] for _ in range(n)]

counter = Counter(files)
sorted_files = sorted(counter.items(), key=lambda x:x[0])

for file in sorted_files:
    print(file[0], file[1])