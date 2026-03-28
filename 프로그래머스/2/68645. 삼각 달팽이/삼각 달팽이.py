def solution(n):
    answer = []
    '''
    삼각형 배열을 만든다
    숫자 1부터 시작
    방향 3개를 반복
    이동 칸 수는 n, n-1, ..., 1
    이동할 때마다 현재 위치에 숫자를 채운다
    마지막에 2차원 삼각형을 1차원으로 펴서 반환한다
    '''
    # 아래, 오른쪽, 왼쪽 위
    dirs = [(1, 0), (0, 1), (-1, -1)]
    arr = [] # [[0], [0,0], [0,0,0], [0,0,0,0]]
    for i in range(1, n + 1):
        arr.append([0] * i)
    
    dir_idx = 0
    r, c = -1, 0
    num = 1
    
    for moves in range(n, 0, -1): # 이동 칸 수는 n, n-1, ..., 1
        for i in range(moves):
            r += dirs[dir_idx][0]
            c += dirs[dir_idx][1]
            arr[r][c] = num
            num += 1
        dir_idx = (dir_idx + 1) % 3
    
    for row in arr:
        answer.extend(row)
        
    return answer