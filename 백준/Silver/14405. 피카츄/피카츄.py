s = input()

words = ["pi", "ka", "chu"]

for word in words:
    s = s.replace(word, ' ')

print('YES') if s.isspace() else print('NO')
