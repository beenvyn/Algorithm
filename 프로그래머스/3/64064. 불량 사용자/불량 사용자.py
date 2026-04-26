def solution(user_id, banned_id):
    candidates = [] # banned_id 별 가능한 id 후보
    
    for b_id in banned_id:
        arr = []
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
                
            flag = True
            for u, b in zip(u_id, b_id):
                if b != '*' and u != b:
                    flag = False
                    break

            if flag:
                arr.append(u_id)
        candidates.append(arr)
    
    result = set()
    # 몇 번 째 banned_id 인지, 지금까지 고른 id
    def dfs(idx, chosen):
        if idx == len(banned_id):
            result.add(frozenset(chosen)) # set를 set에 넣기 위해 frozenset 사용
            return
        
        for user in candidates[idx]:
            if user not in chosen:
                chosen.add(user)
                dfs(idx + 1, chosen)
                chosen.remove(user)
        
    dfs(0, set())
    
    return len(result)