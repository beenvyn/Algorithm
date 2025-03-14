n = int(input())
answer = []
arr = [input() for _ in range(n)]

for x in arr:
    temp = ''
    r, word = x.split()
    for c in word:
        temp += c * int(r)
    answer.append(temp)

for x in answer:
    print(x)