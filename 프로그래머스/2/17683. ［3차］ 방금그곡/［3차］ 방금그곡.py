def solution(m, musicinfos):
    answer = []
    
    def get_mins(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m
    
    # 음의 길이를 맞춰줌 (C#이 음 두개가 아니라 하나로 처리될 수 있게)
    def normalize(s):
        return (s.replace("C#", "c")
                 .replace("D#", "d")
                 .replace("F#", "f")
                 .replace("G#", "g")
                 .replace("A#", "a"))

    m = normalize(m)
    parsed_infos = [] # 제목, 악보, 재생시간
    
    # 악보 전처리
    for idx, info in enumerate(musicinfos):
        s, e, title, notes = info.split(',')
        played = get_mins(e) - get_mins(s)
        
        notes = normalize(notes)
        n = len(notes)
        
        # 재생시간 만큼 늘리기
        base = notes # 원본 저장
        if played > n:
            q, r = divmod(played, n)
            notes += base * q + base[:r]
        else:
            notes = base[:played]
            
        parsed_infos.append([title, notes, played, idx])
    
    # 악보가 m을 포함하는지 확인
    for title, notes, played, idx in parsed_infos: 
        if m in notes:
            answer.append([played, idx, title])
                    
    answer.sort(key=lambda x:(-x[0], x[1]))
        
    return answer[0][-1] if answer else "(None)"