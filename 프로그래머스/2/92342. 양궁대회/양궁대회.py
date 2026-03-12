def solution(n, info):
    answer = [-1]
    lion = [0] * 11
    best_diff = 0
    
    def is_better(new, current):
        # 낮은 점수를 더 많이 맞힌 경우가 우선
        for i in range(10, -1, -1):
            if new[i] > current[i]:
                return True
            elif new[i] < current[i]:
                return False
        return False
    
    # 현재 보고있는 점수 칸, 남은 화살 수
    def dfs(idx, arrows_left):
        nonlocal best_diff, answer
        
        # 모든 점수칸을 다 본 경우
        if idx == 11:
            # 남은 화살은 0점에 몰아주기
            lion[10] += arrows_left 
            
            apeach_score = 0
            lion_score = 0
            
            for i in range(11):
                score = 10 - i
                if info[i] == 0 and lion[i] == 0:
                    continue
                if info[i] < lion[i]:
                    lion_score += score
                else:
                    apeach_score += score
                    
            diff = lion_score - apeach_score
            
            if diff > 0:
                if diff > best_diff:
                    best_diff = diff
                    answer = lion[:]
                elif diff == best_diff and is_better(lion, answer):
                    answer = lion[:]
            
            # 원상 복구
            lion[10] -= arrows_left 
            return
        
        # 해당 점수 선택하기(이기기)
        need = info[idx] + 1
        if need <= arrows_left:
            lion[idx] = need
            dfs(idx + 1, arrows_left - need)
            lion[idx] = 0
        
        # 해당 점수 포기하기(지기)
        dfs(idx + 1, arrows_left)
    
    dfs(0, n)
    return answer