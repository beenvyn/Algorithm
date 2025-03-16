from collections import Counter

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
zip_arr = list(zip(*arr))

answer = ''
cnt = 0

for col in zip_arr:
    counter = Counter(col)
    answer += sorted(counter.keys(), key=lambda x:(-counter[x], x))[0]
   
for word in arr:
    for idx in range(m):
        if word[idx] != answer[idx]:
            cnt += 1

print(answer)
print(cnt)