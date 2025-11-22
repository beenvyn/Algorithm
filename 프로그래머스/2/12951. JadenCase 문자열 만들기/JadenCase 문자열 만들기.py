def solution(s):
    answer = []
    arr = s.split(' ')
    for word in arr:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append('')
    
    return ' '.join(answer)