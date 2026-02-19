def solution(files):
    answer = []
    # head, number 분리
    def parse(file):
        num_start = 0
        while num_start < len(file) and not file[num_start].isdigit():
            num_start += 1
        
        num_end = num_start
        while num_end < len(file) and file[num_end].isdigit() and num_end - num_start < 5:
            num_end += 1
        
        head = file[:num_start]
        number = file[num_start:num_end]
        return head, number
    
    parsed_files = []
    for file in files:
        head, number = parse(file)
        parsed_files.append((head.lower(), int(number), file))
    
    parsed_files.sort(key=lambda x:(x[0], x[1]))
    
    return [f[2] for f in parsed_files]