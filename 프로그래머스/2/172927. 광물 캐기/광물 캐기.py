def solution(picks, minerals):
    answer = 0
    
    total_picks = sum(picks) * 5
    if len(minerals) > total_picks: #  곡괭이 보다 광물이 많은 경우
        minerals = minerals[:total_picks] # 곡괭이로 캘 수 있는 만큼만 자른다
    
    # 광물 5개씩 묶어서 다이아, 철, 돌 갯수 세기
    mineral_groups = [[0,0,0] for _ in range(len(minerals) // 5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            mineral_groups[i//5][0] += 1
        elif minerals[i] == 'iron':
            mineral_groups[i//5][1] += 1
        elif minerals[i] == 'stone':
            mineral_groups[i//5][2] += 1
    
    mineral_groups.sort(key=lambda x:(-x[0], -x[1], -x[2])) # 난이도가 어려운 순으로 정렬
    
    # 정렬된 광물들을 다이아, 철, 돌 곡괭이 순서대로 캔다.
    for group in mineral_groups:
        dia, iron, stone = group
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0: # 다이아 곡괭이
                answer += dia + iron + stone
                picks[j] -= 1
                break
            elif picks[j] > 0 and j == 1: # 철 곡괭이
                answer += (dia * 5) + iron + stone
                picks[j] -= 1
                break
            elif picks[j] > 0 and j == 2: # 돌 곡괭이
                answer += (dia * 25) + (iron * 5) + stone
                picks[j] -= 1
                break
    
    return answer