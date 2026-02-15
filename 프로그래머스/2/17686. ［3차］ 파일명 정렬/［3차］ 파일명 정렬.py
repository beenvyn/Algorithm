def solution(files):
    answer = []

    def parse(file):
        # 숫자 시작 위치 찾기
        start = 0
        while start < len(file) and not file[start].isdigit():
            start += 1
        
        # 숫자 최대 5자리 추출
        end = start
        while end < len(file) and file[end].isdigit() and end - start < 5:
            end += 1
        
        head = file[:start]
        number = file[start:end]
        return head, number
    
    parsed_files = []
    for file in files:
        head, number = parse(file)
        parsed_files.append((head.lower(), int(number), file)) # 원본 저장
    
    parsed_files.sort(key=lambda x:(x[0], x[1]))
    
    return [ x[2] for x in parsed_files ]