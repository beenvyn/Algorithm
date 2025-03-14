word = input()
answer = []
alp = 'abcdefghijklmnopqrstuvwxyz'

for a in alp:
    answer.append(word.find(a))

print(*answer)