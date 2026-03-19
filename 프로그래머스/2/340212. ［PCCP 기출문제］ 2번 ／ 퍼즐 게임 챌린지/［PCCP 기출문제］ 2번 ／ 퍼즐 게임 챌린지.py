def solution(diffs, times, limit):
    
    # 제한 시간 내에 풀 수 있는지 판단하는 함수
    def solve(level):
        total = times[0]
        
        for i in range(1, len(diffs)):
            total += times[i] # 기본 푸는 시간
            diff = diffs[i]
            if level < diff:
                wrong = diff - level
                total += (times[i] + times[i-1]) * wrong
        
        if total <= limit:
            return True
        else:
            return False
    
    # 이분 탐색으로 정답 후보를 탐색
    # level이 작아질수록 총 시간이 커지고, 커질수록 총 시간이 줄어들기 때문에 이분 탐색이 가능
    l, r = 1, max(diffs)
    while l <= r:
        mid = (l + r) // 2
        
        if solve(mid): # 가능하면
            answer = mid
            r = mid - 1 # 더 낮은 레벨로도 가능한지 확인
        else:
            l = mid + 1
        
    return answer