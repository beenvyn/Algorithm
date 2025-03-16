a, b = input().split()
count = []
current = 0

while current <= len(b) - len(a):
    cnt = 0
    word = b[current:current + len(a)]
    for w in zip(a, word):
        if w[0] != w[1]:
            cnt += 1
    count.append(cnt)
    current += 1

print(min(count))