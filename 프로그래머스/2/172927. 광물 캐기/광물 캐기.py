def solution(picks, minerals):
    answer = 0
    pick_idx = 0
    fatigue_dict = {'diamond': [1, 5, 25], 'iron': [1, 1, 5], 'stone': [1, 1, 1]}
    max_minerals = sum(picks) * 5

    groups = [minerals[i:i+5] for i in range(0, max_minerals, 5)] # 5개씩 묶음
    groups_cnt = [[idx, 0, 0, 0] for idx in range(len(groups))] # 묶음별 인덱스, 다이아 곡갱이 수, 철 곡갱이 수, 돌 곡갱이 수
    
    for i in range(len(groups)):
        for m in groups[i]:
            if m == 'diamond':
                groups_cnt[i][1] += 1
            elif m == 'iron':
                groups_cnt[i][2] += 1
            else:
                groups_cnt[i][3] += 1
    
    groups_cnt.sort(key=lambda x:(-x[1], -x[2], -x[3])) # 난이도 어려운 순으로 정렬
    
    for i in range(len(groups_cnt)):
        cur_minerals = groups[groups_cnt[i][0]]
        while pick_idx < 3 and picks[pick_idx] == 0:
            pick_idx += 1
        for m in cur_minerals:
            answer += fatigue_dict[m][pick_idx]
        picks[pick_idx] -= 1

    return answer