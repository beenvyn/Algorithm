def solution(relation):
    answers = [] # 후보키를 저장하는 배열 
    attributes = len(relation[0])
    
    # 후보키인지 확인하는 함수
    def check(key):
        # 유일성 확인
        tuples = []
        # key에 해당하는 속성들만 뽑아서 튜플을 만든다.
        for row in relation:
            cur_key = []
            for k in key:
                cur_key.append(row[k])
            tuples.append(tuple(cur_key))
            
        if len(tuples) != len(set(tuples)): # 중복이 있으면
            return False
        
        # 최소성 확인
        for a in answers:
            if set(a).issubset(set(key)): # 이미 구한 후보키가 현재 key의 부분집합이면
                return False
        return True
    
    # 속성 조합 생성
    def comb(idx, cur, length):
        if len(cur) == length:
            if check(cur):
                answers.append(cur)
            return
        
        for i in range(idx, attributes):
            comb(i + 1, cur + [i], length)
        
    # 속성 개수 1개 ~ 전체 개수까지 조합 생성
    for length in range(1, attributes + 1):
        comb(0, [], length)
        
    return len(answers)