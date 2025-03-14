vowels = 'aeiou'

while True:
    answer = 0
    string = input()
    if string == '#':
        break

    for c in string:
        if c in vowels or c in vowels.upper():
            answer += 1
    
    print(answer)