def solution(m, musicinfos):

    def to_mins(string):
        h, m = map(int, string.split(':'))
        return h * 60 + m
    
    parsed_infos = []
    
    for info in musicinfos:
        start, end, title, notes = info.split(',')
        playtime = to_mins(end) - to_mins(start)

        notes = notes.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        n = len(notes)
        if n >= playtime:
            played = notes[:playtime]
        else:
            played = notes * (playtime // n) + notes[:playtime % n]
        
        parsed_infos.append([played, playtime, title])
                
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    answer = ''
    max_p = 0
    
    for info in parsed_infos:
        if m in info[0]:
            if info[1] > max_p:
                max_p = info[1]
                answer = info[2]
        
    return answer if answer else '(None)'