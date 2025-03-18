n = input()
cnt = 0

while len(n) != 1:
    n = str(sum([int(x) for x in n]))
    cnt += 1

print(cnt)
if n in '369':
    print('YES')
else:
    print('NO')