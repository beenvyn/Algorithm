while True:
    s = input()

    if s == 'end':
        break

    vowels = 'aeiou'
    is_acceptable = True # flag 변수
    
    if not any(vowel in s for vowel in vowels):
        is_acceptable = False

    v = 0
    not_v = 0
    for char in s:
        if char in vowels:
            v += 1
            not_v = 0
        else:
            not_v += 1
            v = 0
        
        if v == 3 or not_v == 3:
            is_acceptable = False
            break
            
    
    for i in range(len(s) - 1):
        if s[i] == s[i+1] and s[i] not in ['e', 'o']:
            is_acceptable = False
            break
    
    if is_acceptable:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')