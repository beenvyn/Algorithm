
def solution(id_list, report, k):
    report_set = set(report)
    answer = [0] * len(id_list)
    
    # id별 신고 당한 횟수
    reports = {id: 0 for id in id_list}
    for r in report_set:
        reports[r.split()[1]] += 1
    
    # 신고 한 사람 - 신고 당한 사람 목록을 돌면서 신고 당한 사람의 이용 정지 여부 확인 -> 이용 정지된 거면 메일 횟수 증가
    for r in report_set:
        # 이용 정지된 사람 찾기 
        if reports[r.split()[1]] >= k:
            # 신고자의 메일 받는 횟수를 1 증가
            answer[id_list.index(r.split()[0])] += 1
    
    return answer   