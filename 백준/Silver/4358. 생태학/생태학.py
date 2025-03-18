import sys
from collections import Counter

input = sys.stdin.readline
arr = []

while True:
    tree = input().strip()
    if tree == '':
        break
    arr.append(tree)

n = len(arr)
counter = Counter(arr)
answer = {}

for t in counter.items():
    type, cnt = t
    answer[type] = (cnt / n)*100

for x in sorted(answer.keys()):
    print("%s %.4f" % (x , answer[x]))