def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    # 2
    word = ''
    for char in new_id:
        if char.isalpha() or char.isnumeric() or char in '-_.':
            word += char
    
    # 3
    while '..' in word:
        word = word.replace('..','.')
    
    # 4
    if len(word) > 0 and word[0] == '.':
        word = word[1:]
    if len(word) > 0 and word[-1] == '.':
        word = word[:-1]
    
    # 5
    if not word:
        word = 'a'
    
    # 6
    if len(word) >= 16:
        word = word[:15]
        
        if word[-1] == '.':
            word = word[:-1]
        
    # 7
    if len(word) <= 2:
        while len(word) != 3:
            tmp = word[-1]
            word += tmp
    
    return word