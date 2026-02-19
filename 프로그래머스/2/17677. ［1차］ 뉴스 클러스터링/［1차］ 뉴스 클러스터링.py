from collections import Counter

def solution(str1, str2):
    answer = 0
    
    def get_multi_set(s):
        multi_set = []
        s = s.lower()
        
        for i in range(len(s) - 1):
            x = s[i:i+2]
            if x.isalpha():
                multi_set.append(x)
        return multi_set
    
    str1_counter = Counter(get_multi_set(str1))
    str2_counter = Counter(get_multi_set(str2))
    
    inter = str1_counter & str2_counter
    union = str1_counter | str2_counter
    
    inter_size = sum(inter.values())
    union_size = sum(union.values())
    
    if union_size == 0:
        return 65536
    
    return int((inter_size / union_size) * 65536)