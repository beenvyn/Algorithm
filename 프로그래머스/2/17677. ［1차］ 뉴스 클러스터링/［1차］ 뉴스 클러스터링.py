from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 다중집합 만들기
    def multi_set(s):
        s = s.upper()
        res = []
        for i in range(len(s) -1):
            word = s[i:i+2]
            if word.isalpha():
                res.append(word)
        return res
        
    A = Counter(multi_set(str1))
    B = Counter(multi_set(str2))
    
    inter = A & B # 같은 원소가 있으면 "최소 개수"만 남김
    union = A | B # 같은 원소 있으면 "최대 개수" 유지
    
    inter_size = sum(inter.values())
    union_size = sum(union.values())
        
    if union_size == 0: # 2글자 알파벳 조합이 하나도 없을 때
        return 65536
    
    return int(inter_size / union_size * 65536)