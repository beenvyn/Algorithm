def solution(rows, cols, board):
    answer = 0
    board = [list(row) for row in board]
    dirs = [(0, 1), (1, 0), (1, 1)]
    
    # 블록 구하는 함수
    def find_block():
        coords = set()
        
        for r in range(rows - 1):
            for c in range(cols - 1):
                x = board[r][c] # 정사각형의 왼쪽 위 꼭짓점
                if x == '0': # 빈 공간인 경우 
                    continue
                    
                flag = True
                dir_idx = 0
                while flag and dir_idx < 3:
                    nr, nc = r + dirs[dir_idx][0], c + dirs[dir_idx][1]
                    if board[nr][nc] != x: # 다르면 바로 탈락
                        flag = False
                        break
                    dir_idx += 1
                if flag:
                    coords.add((r, c))
                    for d in dirs:
                        coords.add((r + d[0], c + d[1]))
        return coords
    
    # 판 바꾸는 함수
    def change_board(coords):
        nonlocal board
        
        new_board = [row[:] for row in board]
        
        # 빈 공간 '0'으로 바꾸기
        for r, c in coords:
            new_board[r][c] = '0'
        
        # 떨어뜨리기
        for c in range(cols):
            empty_row = rows - 1 # 현재 채워야 할 가장 아래 위치
            for r in range(rows - 1, -1, -1):
                if new_board[r][c] != '0': # 블록이 있는 칸만 이동시킴. 빈칸이면 무시
                    new_board[empty_row][c] = new_board[r][c]
                    if r != empty_row: # 만약 블록이 이동했다면 원래 자리를 빈칸으로 만들어 준다
                        new_board[r][c] = '0'
                    empty_row -= 1
            
        board = [row[:] for row in new_board]
    
    while True:
        coords = find_block()
        if not coords:
            break
        
        answer += len(coords)
        change_board(coords)
        
    return answer