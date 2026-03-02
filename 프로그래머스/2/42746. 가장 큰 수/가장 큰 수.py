def solution(numbers):
    # 왼쪽부터 한 글자씩 비교하는 문자열 비교의 특성을 이용
    # 3이랑 30을 비교할 때 330이랑 303중에서 330이 더 크니까 우리는 3이 앞에 오길 원하지만 비교 과정이서는 없음과 0을 비교하면 0이 더 크다고 나오니까 트릭을 사용해야 함.
    # numbers의 원소는 최대 4자리니까 4번 곱해서 비교
    numbers = sorted(numbers, key=lambda x: str(x)*4, reverse=True)
    answer = ''.join(map(str, numbers))
    return answer if int(answer) != 0 else '0' # 모든 숫자가 0인 경우 처리
        
    
    
    