n = int(input())
words = [input() for _ in range(n)]
words = sorted(words, key=lambda x:(x, len(x)))
answer = 0

for i in range(n - 1):
    if words[i + 1].startswith(words[i]):
        answer += 1

print(n - answer)