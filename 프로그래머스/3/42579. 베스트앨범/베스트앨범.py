def solution(genres, plays):
    answer = []
    dic = {}
    
    for idx, g in enumerate(genres):
        if g not in dic:
            dic[g] = []
        dic[g].append(idx)
    
    genre_order = sorted(dic.keys(), key=lambda x: -sum([plays[i] for i in dic[x]]))
    
    for g in genre_order:
        arr = sorted(dic[g], key=lambda x: (-plays[x], x))[:2]
        answer.extend(arr)
    
    return answer