from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = {} # "언어 직군 경력 소울 푸드" ('-' 포함) : [점수1, 점수2 ...]

    # 1. 지원자 정보 저장: 1명 당 '-' 포함한 모든 경우의 키 16개 만들기 (2^4)
    for line in info:
        arr = line.split()
        attrs = arr[:-1]
        score = int(arr[-1])
        
        # '-' 조합 만들기
        for r in range(5): # 0~4개를 '-'로 바꾸는 경우
            for comb in combinations(range(4), r):
                temp = attrs[:]
                for idx in comb:
                    temp[idx] = '-'
                key = ' '.join(temp)
                if key in info_dict:
                    info_dict[key].append(score)
                else:
                    info_dict[key] = [score]
    
    # 2. 각 키별 점수 리스트 정렬 (이분탐색 위해)
    for k in info_dict:
        info_dict[k].sort()
    
    # 정렬된 arr에서 처음으로 target 이상이 되는 인덱스를 찾는다
    # 예) arr = [50, 80, 80, 150, 210], target = 80
    #     return 1  
    def lower_bound(arr, target):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l     
    
    # 3. 쿼리 처리
    for q in query:
        q = q.replace(' and ', ' ')
        arr = q.split()
        key = ' '.join(arr[:-1])
        score = int(arr[-1])
        
        scores = info_dict.get(key, [])  # 해당 조건에 해당하는 점수 리스트
        idx = lower_bound(scores, score) # score 이상이 시작되는 인덱스
        answer.append(len(scores) - idx) # 그 뒤에 남은 개수 = score 이상 개수
        
    return answer