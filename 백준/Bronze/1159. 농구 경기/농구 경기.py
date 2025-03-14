from collections import Counter

n = int(input())
answer = ''
arr = [input()[0] for _ in range(n)]
counter = Counter(arr)

for item in sorted(counter.items()):
    if item[1] >= 5:
        answer += item[0]

print(answer) if answer else print('PREDAJA')
