i = 1

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    answer = (v // p) * l + min((v % p), l)
    print(f'Case {i}: {answer}')
    i += 1