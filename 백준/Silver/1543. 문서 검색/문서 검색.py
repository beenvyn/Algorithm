s = input()
f = input()
answer = 0
current = 0

while current <= len(s) - len(f):
    if s[current:current + len(f)] == f:
        answer += 1
        current += len(f)
    else:
        current += 1
    
print(answer)