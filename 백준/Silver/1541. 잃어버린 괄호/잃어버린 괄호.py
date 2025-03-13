s = input().split('-')
result = sum(map(int, s[0].split('+')))

for part in s[1:]:
    result -= sum(map(int, part.split('+')))

print(result)