def solution(s):
    answer = []
    
    parts = s[2:-2].split('},{')
    sets = [set(map(int, p.split(','))) for p in parts]
    sets.sort(key=len)
    
    seen = set()
    for st in sets:
        new = st - seen
        answer += list(new)
        seen.update(new)
                
    return answer